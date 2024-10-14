import load_data
import print_util
import constant


def get_user_input_command(message: str) -> str:
    input_available_commands = ""
    while True:
        try:
            input_available_commands = (input(message))

            if ("help" not in input_available_commands
                    and "show_countries" not in input_available_commands
                    and "top_countries" not in input_available_commands):
                raise ValueError()

        except ValueError:
            print(f"Unknown command {input_available_commands}")
        else:
            break

    return input_available_commands


def show_countries(number: int):
    for country in sorted(set(call_load_data())):
        print(country)

    call_user_input()


def top_countries(number_countries: int):
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


def call_load_data():
    return [dta[constant.COUNTRY_KEY] for dta in load_data.fetch_data()[constant.BASE_KEY]]


def call_user_input():
    print("")
    select_options(get_user_input_command(""))


def split_choice(user_choice: str):
    top_countries, number = user_choice.split(" ")
    return top_countries, number


def select_options(user_choice: str) -> None:
    func_dict = {f"{constant.HELP}": print_util.display_options,
                 f"{constant.SHOW_COUNTRIES}": show_countries,
                 f"{constant.TOP_COUNTRIES_V2}": top_countries
                 }

    if "help" in user_choice or "show_countries" in user_choice:
        func_dict[user_choice](0)
    else:
        option, parameter = split_choice(user_choice)
        func_dict[option](parameter)
