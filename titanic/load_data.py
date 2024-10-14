import json

FILE_PATH = "ships_data.json"

cached_data = None


def load_data():
    """ Loads a JSON file """
    with open(FILE_PATH, "r") as handle:
        return json.load(handle)


def fetch_data():
    global cached_data
    if cached_data is None:
        cached_data = load_data()
    return cached_data
