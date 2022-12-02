import yaml
import os

# local module imports


def make_data_path(direction: str, file_name: str, config: dict) -> str:
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


class Config():
    """Class to hold the config file as a dict"""
    def __init__(self, config_path: str):
        self.config_path = config_path

    def load_config(self):
        """Loads the config file as a dict"""
        with open(self.config_path, 'r') as f:
            return yaml.safe_load(f)


# Load config file as a dict
config = Config("config.yaml").load_config()