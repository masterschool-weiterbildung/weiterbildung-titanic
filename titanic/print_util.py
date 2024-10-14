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


def display_options(number):
    """
    Displays the available commands and prompts the user for input.

    Parameter:
        number (int): Currently unused in the function but can be passed as an argument.

    Returns:
        None
    """
    print("Available commands:")
    print(f"{constant.HELP}")
    print(f"{constant.SHOW_COUNTRIES}")
    print(f"{constant.TOP_COUNTRIES}\n")

    input_util.select_options(input_util.get_user_input_command(""))
