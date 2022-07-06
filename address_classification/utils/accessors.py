"""
Author: Claire Baxter
Date: 04/07/2021
Description: Module containing functionality for loading the data

Possible future expansions:
- Adding functionality for combining datasets
- Could use something else instead of pandas e.g. pyspark.sql dataframes
"""

import pandas as pd
import yaml


def load_data(path: str, file_name: str) -> pd.DataFrame:
    """
    Function for loading a single dataset into a pandas dataframe.

    Args:
        path (str): Path to file
        file_name (str): Name of the file

    Returns:
        pd.dataframe: Pandas dataframe of data
    """

    # Extract the file type extension from file_name
    ft = file_name.split('.')[-1]

    # Load the file as pandas dataframe
    if 'json' in ft:
        if 'l' in ft:
            df = pd.read_json(path + file_name, lines=True)
        else:
            df = pd.read_json(path + file_name)
    else:
        raise NotImplementedError("Filetype '{}' not implemented yet.".format(ft))

    return df


def get_config(config_path: str):
    """
    Function to load the configuration file.

    Args:
        config_path (str): Path to config file

    Returns:
        config (dict): Dictionary containing configuration information for a feature.
    """

    try:
        with open(config_path, "r") as f:
            config = yaml.load(f, Loader=yaml.FullLoader)

    except Exception as e:
        raise ValueError("Could not load log file due to error: {0}".format(e))

    return config