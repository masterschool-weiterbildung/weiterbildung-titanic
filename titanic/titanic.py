import print_util
import input_util


def main():
    """
    The main entry point for the Ships CLI application.

    Returns:
        None
    """
    print_util.print_introduction()

    input_util.select_options(input_util.get_user_input_command(""))


if __name__ == '__main__':

    main()
