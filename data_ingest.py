def call_api (locs, parameters):
  """
  Call api to gain public and private travel times

  Args: 
    locs (list): A list of dictionaries containing locations.
        Must contain keys ["id", "coords"].
    parameters (dict): A dictionary of parameters for the api call
    
  Returns:
    api_data (dict): A dictionary of public transport arrival locations and travel times

  """
  # Call the API
  api_data = ttpy.time_filter_fast(locations=locs, arrival_one_to_many=parameters)
  
  return api_data