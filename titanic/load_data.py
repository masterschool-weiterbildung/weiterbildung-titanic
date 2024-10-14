import json

FILE_PATH = "ships_data.json"
cached_data = None


def load_data() -> dict:
    """
    Loads and returns the content of a JSON file.

    Returns:
        dict: The data loaded from the JSON file.
    """
    with open(FILE_PATH, "r") as handle:
        return json.load(handle)


def fetch_data() -> dict:
    """
    Fetches the data, caching it after the first load.
    This shows the Singleton Pattern.
    Following the standard for API invocation

    Returns:
        dict: The cached or freshly loaded data from the JSON file.
    """
    global cached_data
    if cached_data is None:
        cached_data = load_data()
    return cached_data
