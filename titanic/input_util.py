from typing import List

import load_data
import print_util
import constant


def call_load_data() -> list:
    """
    Fetches data using the `load_data.fetch_data()` method

    Returns:
        list: A list of country data extracted from the loaded data.
    """
    return [dta[constant.COUNTRY_KEY] for dta in
            load_data.fetch_data()[constant.BASE_KEY]]


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
    Splits the given user choice string by spaces and returns a list of individual words.

    Parameter:
        user_choice (str): The user input string to be split.

    Returns:
        list[str]: A list of words resulting from splitting the user input by spaces.
    """
    return user_choice.split(" ")


def get_user_input_command(message: str) -> str:
    """
    Prompts the user for input and validates the command entered.

    Parameter:
        message (str): The message or prompt to display to the user when asking for input.

    Returns:
        str: The validated user input command.

    Raises:
        ValueError: If the entered input does not match any of the allowed commands.

    Example:
        user_input = get_user_input_command("")
    """
    input_available_commands = ""
    while True:
        try:
            input_available_commands = (input(message))

            if (constant.HELP not in input_available_commands
                    and constant.SHOW_COUNTRIES
                    not in input_available_commands
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
    Displays a sorted list of unique countries fetched from the data, then prompts the user for input.

    Parameter:
        number (int): Dummy parameter

    Returns:
        None
    """
    for country in sorted(set(call_load_data())):
        print(country)

    call_user_input()


def top_countries(number_countries: int):
    """
    Displays the top countries based on the number of occurrences in the dataset.

    Parameter:
        number_countries (int): The number of top countries to display.

    Returns:
        None
    """
    countries = {}

    for country in call_load_data():
        if country in countries:
            countries[country] += 1
        else:
            countries[country] = 1

    sorted_countries = sorted(countries.items(),
                              key=lambda country: country[1], reverse=True)

    for country, count in sorted_countries[:int(number_countries)]:
        print(f"{country} : {count}")

    call_user_input()


def select_options(user_choice: str) -> None:
    """
    Selects and executes a function based on the user's command.
    Utilize Dispatch Table Pattern

    Parameter:
        user_choice (str): The command input by the user, which determines which function to call.

    Example:
        select_options("show_countries")
        select_options("top_countries 5")
    """
    func_dict = {f"{constant.HELP}": print_util.display_options,
                 f"{constant.SHOW_COUNTRIES}": show_countries,
                 f"{constant.TOP_COUNTRIES_V2}": top_countries
                 }

    if "help" in user_choice or "show_countries" in user_choice:
        func_dict[user_choice](0)
    else:
        option, parameter = split_choice(user_choice)
        func_dict[option](parameter)
