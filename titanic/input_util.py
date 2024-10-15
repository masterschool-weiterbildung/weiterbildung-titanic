import load_data
import print_util
import constant
import map_util


def call_user_input() -> None:
    """
    Prompts the user for input via `get_user_input_command`.
    The user's command is passed to `select_options` for further processing.

    Returns:
        None
    """
    print("")
    select_options(get_user_input_command(""))


def split_choice(user_choice: str) -> list[str]:
    """
    Splits the given user choice string by spaces and returns a list
    of individual words.

    Parameter:
        user_choice (str): The user input string to be split.

    Returns:
        list[str]: A list of words resulting from splitting the user
        input by spaces.
    """
    return user_choice.split(" ")


def get_user_input_command(message: str) -> str:
    input_available_commands = ""
    while True:
        try:
            input_available_commands = (input(message))

            option = [constant.HELP,
                      constant.SHOW_COUNTRIES,
                      constant.TOP_COUNTRIES_V2,
                      constant.SHIPS_BY_TYPE,
                      constant.SEARCH_SHIP,
                      constant.SPEED_HISTOGRAM,
                      constant.DRAW_MAP]

            if (input_available_commands not in option
                    and constant.TOP_COUNTRIES_V2
                    not in input_available_commands):
                raise ValueError()

        except ValueError:
            print(f"Unknown command {input_available_commands}")
        else:
            break

    return input_available_commands


def show_countries(number: int) -> None:
    """
    Displays a sorted list of unique countries fetched from the
    data, then prompts the user for input.

    Parameter:
        number (int): Dummy parameter

    Returns:
        None
    """
    for country in sorted(set(load_data.call_load_data())):
        print(country)

    call_user_input()


def top_countries(number_countries: int) -> None:
    """
    Displays the top countries based on the number of occurrences in
    the dataset.

    Parameter:
        number_countries (int): The number of top countries to display.

    Returns:
        None
    """
    countries = {}

    for country in load_data.call_load_data():
        if country in countries:
            countries[country] += 1
        else:
            countries[country] = 1

    sorted_countries = sorted(countries.items(),
                              key=lambda country: country[1], reverse=True)

    for country, count in sorted_countries[:int(number_countries)]:
        print(f"{country} : {count}")

    call_user_input()


def ships_by_types(number: int) -> None:
    [print(type_ship)
     for type_ship in sorted(set(load_data.call_type_ship_load_data()))]

    call_user_input()


def search_ship(number: int):
    input_ship_name = input("Enter Ship name: ")

    [print(type_ship)
     for type_ship in sorted(set(load_data.call_search_ship_load_data()))
     if input_ship_name.lower() in type_ship.lower()]

    call_user_input()


def speed_histogram(number: int) -> None:
    map_util.draw_ship_histogram()

    call_user_input()


def draw_map(number: int) -> None:
    map_util.draw_map()

    call_user_input()


def select_options(user_choice: str) -> None:
    """
    Selects and executes a function based on the user's command.
    Utilize Dispatch Table Pattern

    Parameter:
        user_choice (str): The command input by the user, which determines
        which function to call.

    Example:
        select_options("show_countries")
        select_options("top_countries 5")
    """
    func_dict = {f"{constant.HELP}": print_util.display_options,
                 f"{constant.SHOW_COUNTRIES}": show_countries,
                 f"{constant.TOP_COUNTRIES_V2}": top_countries,
                 f"{constant.SHIPS_BY_TYPE}": ships_by_types,
                 f"{constant.SEARCH_SHIP}": search_ship,
                 f"{constant.SPEED_HISTOGRAM}": speed_histogram,
                 f"{constant.DRAW_MAP}": draw_map
                 }

    option = [constant.HELP,
              constant.SHOW_COUNTRIES,
              constant.SHIPS_BY_TYPE,
              constant.SEARCH_SHIP,
              constant.SPEED_HISTOGRAM,
              constant.DRAW_MAP]

    if user_choice in option:
        func_dict[user_choice](0)
    else:
        option, parameter = split_choice(user_choice)
        func_dict[option](parameter)
