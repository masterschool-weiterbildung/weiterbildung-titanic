import json
import constant

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
    Fetches the data and caches it after the first load,
    demonstrating the Singleton Pattern and
    following the standard for API invocation

    Returns:
        dict: The cached or freshly loaded data from the JSON file.
    """
    global cached_data

    if cached_data is None:
        cached_data = load_data()
    return cached_data


def call_load_data() -> list:
    """
    Fetches data using the `load_data.fetch_data()` method

    Returns:
        list: A list of country data extracted from the loaded data.
    """
    return [dta[constant.COUNTRY_KEY] for dta in
            fetch_data()[constant.BASE_KEY]]


def call_type_ship_load_data() -> list:
    """
    Retrieves a list of ship type summaries from the loaded dataset.

    Returns:
        list: A list of ship type summaries.
    """
    return [dta[constant.TYPE_SUMMARY_KEY] for dta in
            fetch_data()[constant.BASE_KEY]]


def call_search_ship_load_data() -> list:
    """
    Retrieves a list of ship names from the loaded dataset.

    Returns:
        list: A list of ship names.
    """
    return [dta[constant.SHIP_NAME] for dta in
            fetch_data()[constant.BASE_KEY]]


def call_search_ship_histogram_load_data() -> list:
    """
    Retrieves a list of ship speeds for histogram plotting
    from the loaded dataset.

    Returns:
        list: A list of ship speeds.
    """
    return [dta[constant.SHIP_SPEED] for dta in
            fetch_data()[constant.BASE_KEY]]


def call_search_ship_lat_lon_load_data() -> list:
    """
    Retrieves a list of ship names and their coordinates
    (latitude and longitude) from the dataset.

    Returns:
        list: A list of lists, where each inner list contains:
              [ship name, longitude, latitude].
    """
    return [[dta[constant.SHIP_NAME], dta[constant.LONGITUDE],
             dta[constant.LATITUDE]] for dta in
            fetch_data()[constant.BASE_KEY]]
