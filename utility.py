def make_data_path(direction: str, file_name: str, config=config):
    """Creates the path for the data files to be read or written from.

    Args:
        direction (str): Either in or out
        file_name (str): Name of the file to be read or written to
        config (dict): Dict derived from the config file

    Returns:
        str: Relative path of the file to be read or written to
    """
    dir_dict = {"in": config["input_data"]["input_folder"],
                "out": config["output_data"]["output_folder"]}
    rel_path = os.path.join(dir_dict[direction], file_name)

    return rel_path
