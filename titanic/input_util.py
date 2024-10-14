from load_data import load_data
import print_util
import constant

def get_user_input_command(message) -> str:
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


def show_countries(number):
    unique_country = set()
    for dta in load_data()['data']:
        unique_country.add(dta['COUNTRY'])

    for country in sorted(list(unique_country)):
        print(country)

    print("")
    select_options(get_user_input_command(""))


def top_countries(number):
    locations = [dta['COUNTRY'] for dta in load_data()['data']]

    counts = {location: locations.count(location) for location in set(locations)}

    sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))

    print(sorted_counts)

def main():
    top_countries(3)

if __name__ == '__main__':
    main()


def split_choice(user_choice):
    top_countries, number = user_choice.split(" ")
    return top_countries, number


def select_options(user_choice):
    func_dict = {f"{constant.HELP}": print_util.display_options,
                 f"{constant.SHOW_COUNTRIES}": show_countries,
                 f"{constant.TOP_COUNTRIES_V2}": top_countries
                 }

    if "help" in user_choice or "show_countries" in user_choice:
        func_dict[user_choice](0)
    else:
        option, parameter = split_choice(user_choice)
        func_dict[option](parameter)
