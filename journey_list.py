# Journeys

 # Journeys can be point to point (A-B) or multi-point (A-B-C...). 
 # We can map 2, 3 and 4 point journeys, using combinations
 # We should look at some kind of route optimisation (manual at this stage). People are unlikely to make time-wasting journeys
 # The journeys should be similar in distance in the datasets

from Call_API_code import locations
from itertools import combinations
import random 

#create random sample of locations, 25 locations to give 625 journeys between each point
locations_samp = random.sample(locations, 25)

#Create all point to point journeys from 25 random locations
a_to_b_journeys = combinations(locations_samp, 2)

#Call API to get A to B journey times
def get_results_from_api(journeys):
    """
    Calls the TravelTime API and returns the results in a dictionary.

    Args:
      journeys (list): A list of tuples containing journeys from A to B.
        Must contain keys ["id", "coords"].
      dep_search (dict): A dictionary of departure locations. Must contain keys
        ["id", "departure_location_id", "arrival_location_ids",
          "transportation","departure_time", "travel_time",
                                      "properties", "range"]

    Returns:
      dict: A dictionary of results.
    """
    #departure and arrival need to be first and second respectively in the list of tuples
    departure_loc = journeys[0]["id"]
    arrival_loc = journeys[1]["id"]

    # Define parameters in dictionary for API call

    public_parameters = {
      "id": "arrive-at one-to-many search example",
      "arrival_location_ids": arrival_loc,
      "departure_location_id": departure_loc,
      "transportation": {"type": "public_transport"},
      "arrival_time_period": "weekday_morning",
      "travel_time": 3600,
      "properties": ["travel_time"]
      }

    private_parameters = {
    "id": "arrive-at one-to-many search example",
    "arrival_location_ids": arrival_loc,
    "departure_location_id": departure_loc,
    "transportation": {"type": "driving"},
    "arrival_time_period": config["api_call_variables"]["arrival_time_period"],
    "travel_time": config["api_call_variables"]["travel_time"],
    "properties": ["travel_time"]
    }

    # Call the API - need to change one_to_many to matrix?
    public_api_data = ttpy.time_filter_fast(a_to_b_journeys=journeys, arrival_one_to_many=public_parameters)
    private_api_data = ttpy.time_filter_fast(a_to_b_journeys=journeys, arrival_one_to_many=private_parameters)

    API_call_time = time.ctime()

    # Define empty results dictionary to store results
    res_dict = {"Start": [], "Destination": [], "Public_Travel_Duration": [],
            "Private_Travel_Duration": [], "API_call_time": [], "Location": [],
            "Arrival_Time_Period": []}
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


