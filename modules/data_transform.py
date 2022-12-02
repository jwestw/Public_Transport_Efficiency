import pandas as pd
from utility import config

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

    df = pd.DataFrame({"id": df_in["id"], "coords": df_in[["lat", "lng"]].to_dict("records")})
    locations_list = df.to_dict('records')

    return locations_list


def process_api_data(public_api_data, private_api_data, departure, config=config):
    """
    Processes api data into a data frame

    Args:
      public_api_data (dict): A dictionary of public transport arrival locations and travel times
      private_api_data (dict): A dictionary of private trasport arrival locations and travel times
      API_call_time (str): Time of day that API was called
      departure (str): ID departure location

    Returns:
      final_df (df): data frame of all public and private journey times
    """
    # Define empty results dictionary to store results
    res_dict = {"Start": [], "Destination": [], "Public_Travel_Duration": [],
            "Private_Travel_Duration": [], "Location": [],
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
