import input_util
import constant


def print_introduction():
    print("Welcome to the Ships CLI! Enter "
          "'help' to view available commands.")


def display_options(number):
    print("Available commands:")
    print(f"{constant.HELP}")
    print(f"{constant.SHOW_COUNTRIES}")
    print(f"{constant.TOP_COUNTRIES}\n")

    input_util.select_options(input_util.get_user_input_command(""))
