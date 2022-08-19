
import requests
import pandas as pd
import time
import geopandas as gpd
from shapely.geometry import Point
import yaml

import traveltimepy as ttpy
from datetime import datetime
import os

os.environ["TRAVELTIME_ID"] = os.environ.get("TRAVELTIME_ID")
os.environ["TRAVELTIME_KEY"] = os.environ.get("TRAVELTIME_KEY")

def load_config(yaml_path:str):

  with open(yaml_path, 'r') as f:
    return yaml.safe_load(f)

config = load_config("config.yaml")

taunton_locations = [{'id': 'residential 1',
  'coords': {'lat': 51.041757, 'lng': -3.066636}},
 {'id': 'ASDA',
  'coords': {'lat': 51.023503, 'lng': -3.081496}},
 {'id': 'residential 2',
  'coords': {'lat': 51.029702, 'lng': -3.118735}},
 {'id': 'town',
  'coords': {'lat': 51.015169, 'lng': -3.103012}},
 {'id': 'hospital',
  'coords': {'lat': 51.012262, 'lng': -3.119025}},
 {'id': 'college',
  'coords': {'lat': 51.008124, 'lng': -3.091950}},
 {'id': 'primary school',
  'coords': {'lat': 51.035530, 'lng': -3.056741}},
 {'id': 'garden centre',
  'coords': {'lat': 51.040878, 'lng': -3.053207}},
 {'id': 'Aldi',
  'coords': {'lat': 51.026597, 'lng': -3.068437}},
 {'id': 'church',
  'coords': {'lat': 51.050572, 'lng': -3.053070}},
 {'id': 'secondary school',
  'coords': {'lat': 51.035396, 'lng': -3.063187}},
 {'id': 'pub',
  'coords': {'lat': 51.048597, 'lng': -3.056803}}]

def walking_time(meters = 500, speed = 5):
  # To calculate time use formula time = distance / speed
  speed_meters = speed * 1000
  max_walk_time = (meters/speed_meters)*60*60

  return max_walk_time

max_walk_time = walking_time()

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
      "departure_location_ids": arrival_locations,
      "arrival_location_id": departure,
      "transportation": {"type": "public_transport"},
      "arrival_time": datetime.utcnow().isoformat(),
      "travel_time": 3600,
      "properties": ["travel_time", "distance_breakdown"]
      }

    private_parameters = {
    "id": "arrive-at one-to-many search example",
    "departure_location_ids": arrival_locations,
    "arrival_location_id": departure,
    "transportation": {"type": "driving"},
    "arrival_time": datetime.utcnow().isoformat(),
    "travel_time": config["api_call_variables"]["travel_time"],
    "walking_time": max_walk_time,
    "properties": ["travel_time"]
    }

    # Call the API
    public_api_data = ttpy.time_filter(locations=locs, arrival_searches=public_parameters)

    return public_api_data

if config["api_call_variables"]["call_api"] == True:
  api_output_df = get_results_from_api(locs=taunton_locations)

  print(api_output_df)
