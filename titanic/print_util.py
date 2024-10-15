import input_util
import constant


def print_introduction() -> None:
    """
    Prints the introductory message for the Ships CLI.

    Returns:
        None
    """
    print("Welcome to the Ships CLI! Enter "
          "'help' to view available commands.")


def display_options(number: int) -> None:
    """
    Displays the available commands and prompts the user for input.

    Parameter:
        number (int): Currently unused

    Returns:
        None
    """
    print("Available commands:")
    print(f"{constant.HELP}")
    print(f"{constant.SHOW_COUNTRIES}")
    print(f"{constant.TOP_COUNTRIES}")
    print(f"{constant.SHIPS_BY_TYPE}")
    print(f"{constant.SEARCH_SHIP}")
    print(f"{constant.SPEED_HISTOGRAM}")
    print(f"{constant.DRAW_MAP}\n")

    input_util.select_options(input_util.get_user_input_command(""))
