import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import yaml

import traveltimepy as ttpy
import os
from dotenv import load_dotenv

# local module imports
import utility as ut
import geospatial as gs
import data_transform as dt
import data_ingest as di
import data_cleaning as dc
import modules.data_output as dout


load_dotenv('.env')
os.environ["TRAVELTIME_ID"] = os.getenv("TRAVELTIME_ID")
os.environ["TRAVELTIME_KEY"] = os.getenv("TRAVELTIME_KEY")

# Load config file as a dict
config = ut.Config("config.yaml").load_config()

# Make paths
csv_name = config["input_data"]["input_file"]
csv_in = ut.make_data_path("in", csv_name)

hd_name = config["output_data"]["h5_file"]
h5_out_path = ut.make_data_path("out", hd_name)

excel_name = config["output_data"]["output_file"]
excel_out_path = ut.make_data_path("out", excel_name)

# Read in locations data
points_of_interest_df = pd.read_csv(csv_in, delimiter="|", dtype={"POINTX_CLASSIFICATION_CODE": str})

# Subset the dataframe and rename col
locations_df = dc.clean_points_of_interest_df(points_of_interest_df)

# Convert northing and easting -> longnitude and latitude
locations_df = gs.convert_coordinates(locations_df, "FEATURE_EASTING", "FEATURE_NORTHING")

# Create a locations list from the locations dataframe
locations = dt.create_locations_list(locations_df)

# Get the name (or 'id') of the departure location
departure = locations[0]["id"]

# Calculate the max walking time from the max speed
max_walk_time = gs.walking_time()

# Make a list of arrival location names from the locations list
arrival_locations = [locations[index]["id"] for index in range(len(locations))
                     if locations[index]["id"] != departure]

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


if config["api_call_variables"]["call_api"]:
    # Call the API to get the travel times
    public_api_data = di.call_api(locations, public_parameters)
    private_api_data = di.call_api(locations, private_parameters)
    # Process the api data into a dataframe
    api_output_df = dt.process_api_data(public_api_data, private_api_data, departure)
    print(api_output_df)

# Rename df
stored_df = api_output_df

# Check if h5 needs to be written, if not
if config["output_data"]["store_h5"]:
    dout.writeh5(api_output_df, h5_out_path)

# Check write if Excel needs to be written
if config["output_data"]["write_to_excel"]:
    dout.write_excel(stored_df, excel_out_path)
