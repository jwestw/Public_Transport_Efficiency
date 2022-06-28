
import requests
import pandas as pd
import time

import traveltimepy as ttpy
from datetime import datetime
import os

os.environ["TRAVELTIME_ID"] = os.environ.get("TRAVELTIME_ID")london_locations_df = pd.read_csv(r"/Users/chloemurrell/DSST - Public Transport Efficiency/locations_london.csv")

os.environ["TRAVELTIME_KEY"] = os.environ.get("TRAVELTIME_KEY")


london_locations_df = pd.read_csv(r"/Users/chloemurrell/DSST - Public Transport Efficiency/locations_london.csv")

grimsby_locations_df = pd.read_csv(r"/Users/chloemurrell/DSST - Public Transport Efficiency/locations_grimsby.csv")

# Put into function and apply them seperately.
london_locations = []
for index, row in london_locations_csv.iterrows():
    london_locations.append({
            'id': row['Location name'],
            'coords': {'lat': row['Latitude'], 'lng': row["Longnitude"]}
            })

grimsby_locations = []
for index, row in grimsby_locations_csv.iterrows():
    grimsby_locations.append({
            'id': row['Location name'],
            'coords': {'lat': row['Latitude'], 'lng': row["Longnitude"]}
            })


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
      "arrival_time_period": "weekday_morning",
      "travel_time": 3600,
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
        res_dict["API call time"].append(API_call_time)

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

api_output_df_london = get_results_from_api(locs=london_locations)
api_output_df_grimsby = get_results_from_api(locs=grimsby_locations)

print(api_output_df_london)
print(api_output_df_grimsby)

