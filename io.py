"""
Tools that pertain to reading and saving data in data analysis projects
"""

import json
import pickle



def read_config_json(config_path : str):
    with open(config_path, "r") as config_file:
        config = json.load(config_file)
    return config


def read_pickle(pickle_path : str):
    with open(pickle_path, "rb") as pickle_file:
        pickle_content = pickle.load(pickle_file)
    return pickle_content
