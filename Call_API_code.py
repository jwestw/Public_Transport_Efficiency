import requests
import pandas as pd
import time
import geopandas as gpd
from shapely.geometry import Point
import yaml

import traveltimepy as ttpy
from datetime import datetime
import os

os.environ["TRAVELTIME_ID"] = os.environ.get("TRAVELTIME_ID")london_locations_df = pd.read_csv(r"/Users/chloemurrell/DSST - Public Transport Efficiency/locations_london.csv")

os.environ["TRAVELTIME_KEY"] = os.environ.get("TRAVELTIME_KEY")

def load_config(yaml_path:str):
    
  with open(yaml_path, 'r') as f:
    return yaml.safe_load(f)

config = load_config("config.yaml")

points_of_interest_df = pd.read_csv(config["input_data"]["input_path"], delimiter="|", dtype={"POINTX_CLASSIFICATION_CODE":str})

def clean_points_of_interest_df(df_in):

  # Select relevant columns
  df_clean = points_of_interest_df[["NAME", "FEATURE_EASTING", "FEATURE_NORTHING"]]
  # Rename "NAME" column 
  df_clean = df_clean.rename(columns={"NAME":"id"})

  return df_clean

locations_df = clean_points_of_interest_df(points_of_interest_df)

def convert_coordinates(df_in, coord_col_1, coord_col_2):

  # Convert northing and easting -> longnitude and latitude
  geometry = [Point(xy) for xy in zip(df_in[coord_col_1], df_in[coord_col_2])]

  geo_df = gpd.GeoDataFrame(df_in, geometry=geometry)

  geo_df.crs = "EPSG:27700"
  
  geo_df.to_crs("EPSG:4326", inplace=True)

  # Extract lng and lat coodinates into separate columns from POINT() column. 
  geo_df['lng'] = geo_df['geometry'].x
  geo_df['lat'] = geo_df['geometry'].y

  # Convert to pandas df
  pd_df = pd.DataFrame(df_in)

  # Drop unnecessary columns
  pd_df = pd_df.drop([coord_col_1, coord_col_2, "geometry"], axis=1)

  # Rename longnitude column in line with API requirements - delete
  pd_df = pd_df.rename(columns={"lon":"lng"})

  # Add number to end of duplicate id  values
  mask = pd_df['id'].duplicated()
  pd_df.loc[mask, 'id'] += pd_df.groupby('id').cumcount().add(1).astype(str)

  # Drop na values - this occurs do to error in the original spreadsheet which needs fixing
  pd_df = pd_df.dropna(axis=0) 
                            
  return pd_df

locations_df = convert_coordinates(locations_df, "FEATURE_EASTING", "FEATURE_NORTHING")

def create_locations_list(df_in):

  """
  Turns locations df into a list of locations with a dictionary of coordinates.

  Args:
      df_in (pd.DataFrame): dataframe of locations and respective coordinates.
        Should have column names "id", "lat", "lng" which correspond to the location name, 
        latitude and longnitude.

  Returns:
      list: locations_list a list of locations within dictionaries ready for 
        the get_results_from_api function.
  """

  df = pd.DataFrame({"id":df_in["id"], "coords": df_in[["lat", "lng"]].to_dict("records")})
  locations_list = df.to_dict('records')

  return locations_list

locations = create_locations_list(locations_df)


def get_results_from_api(locs):

    """
    Calls the TravelTime API and returns the results in a dictionary.

    Args:
      locs (list): A list of dictionaries containing locations.
        Must contain keys ["id", "coords"].
      dep_search (dict): A dictionary of departure locations. Must contain keys
        ["id", "departure_location_id", "arrival_location_ids",
          "transportation","departure_time", "travel_time",
                                      "properties", "range"]

    Returns:
      dict: A dictionary of results.

    """

    departure = locs[0]["id"]
    arrival_locations = [locs[index]["id"] for index in range(len(locs))
                         if locs[index]["id"] != departure]

    # Define parameters in dictionary for API call

    public_parameters = {
      "id": "arrive-at one-to-many search example",
      "arrival_location_ids": arrival_locations,
      "departure_location_id": departure,
      "transportation": {"type": "public_transport"},
      "arrival_time_period": "weekday_morning",
      "travel_time": 3600,
      "properties": ["travel_time"]
      }

    private_parameters = {
    "id": "arrive-at one-to-many search example",
    "arrival_location_ids": arrival_locations,
    "departure_location_id": departure,
    "transportation": {"type": "driving"},
    "arrival_time_period": config["api_call_variables"]["arrival_time_period"],
    "travel_time": config["api_call_variables"]["travel_time"],
    "properties": ["travel_time"]
    }

    # Call the API 
    public_api_data = ttpy.time_filter_fast(locations=locs, arrival_one_to_many=public_parameters)
    private_api_data = ttpy.time_filter_fast(locations=locs, arrival_one_to_many=private_parameters)

    API_call_time = time.ctime()

    # Define empty results dictionary to store results
    res_dict = {"Start": [], "Destination": [], "Public_Travel_Duration": [],
            "Private_Travel_Duration": [], "API call time": []}
    # number_of_arrival_locations = len(arrival_locations)

    public_refined_api_data = public_api_data["results"][0]["locations"]
    private_refined_api_data = private_api_data["results"][0]["locations"]

    # Loop through destination locations - store journey times into results dictionary.
    for destination_result in public_refined_api_data:
        public_duration_result = destination_result["properties"]["travel_time"]
        destination_name = destination_result["id"]
        res_dict["Start"].append(departure)
        res_dict["Destination"].append(destination_name)
        res_dict["Public_Travel_Duration"].append(public_duration_result)
        res_dict["API_call_time"].append(API_call_time)
        res_dict["Location"].append(config["api_call_variables"]["city_name"])
        res_dict["Arrival_Time_Period"].append(config["api_call_variables"]["arrival_time_period"])
    
    # Ensure public and private destination are the same.
    for index, destination_result in enumerate(private_refined_api_data):
          priv_destination = destination_result["id"]
          pub_dest_same_index = res_dict["Destination"][index]
          if priv_destination != pub_dest_same_index:
                print(f"Public destination: {res_dict['Destination'][index]}, Private Destination: {destination_result['id']}")
                raise
          private_duration_result = destination_result["properties"]["travel_time"]
          res_dict["Private_Travel_Duration"].append(private_duration_result)

    final_df = pd.DataFrame(res_dict)

    return final_df

if config["api_call_variables"]["call_api"] == True:
  api_output_df = get_results_from_api(locs=locations)

  print(api_output_df)


if config["output_data"]["store_h5"] == True:

  store = pd.HDFStore('results.h5')
  store.append("results", api_output_df, append=True)

  store.close()

  store.is_open

store = pd.read_hdf("results.h5")

print(store)

if config["output_data"]["write_to_excel"] == True:
  with pd.ExcelWriter(config["output_data"]["output_path"]) as writer:
      store.to_excel(writer)