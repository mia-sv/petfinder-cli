from tabulate import tabulate
import requests

import common


def find_menu(pet_count, current_page, total_pages):
    return tabulate(
        [
            ["ID", "Option"],
            [f"0-{pet_count  - 1}", "Select a pet to favourite/unfavourite"],
            ["N", f"Next page of buddies ({current_page}/{total_pages})"],
            ["P", f"Previous page of buddies ({current_page}/{total_pages})"],
            ["E", "Exit to menu"],
        ],
        headers="firstrow",
        tablefmt="rounded_outline",
    )


def find(token):
    find_configuration = common.CONFIGURATION
    response = get_animals(token, 1, find_configuration)

    # Gets a set of animal ids from the favourites file.
    favourited_animals = common.get_intset_from_file(common.FAVOURITES_FILE)
 
    # Check if configuration caused errors
    if "animals" not in response:
        print("Failed to fetch results, please check configuration.")
        return

    while True:
        num_total_animals = response["pagination"]["total_count"]
        num_page_animals = len(response["animals"])
        current_page = response["pagination"]["current_page"]
        total_pages = response["pagination"]["total_pages"]

        # We send a set of favourited animals so we can set the (favourited) flag.
        animals_table = tabulate_animals(response["animals"], favourited_animals)

        print(f"Found {num_total_animals} pets.")
        print(animals_table)
        print(find_menu(num_page_animals, current_page, total_pages))

        match input("Choose option: ").upper():
            case num if common.is_int_and_between(num, 0, num_page_animals):
                # Fetches the id from the animal at the index we enter.
                petfinder_id = response["animals"][int(num)]["id"]

                # If the id is already favourited, we unfavourite it.
                if petfinder_id not in favourited_animals:
                    favourited_animals.add(petfinder_id)
                else:
                    favourited_animals.discard(petfinder_id)

                common.save_strset_to_file(
                    favourited_animals, common.FAVOURITES_FILE
                )
            case "N" if current_page < total_pages:
                response = get_animals(token, current_page + 1, find_configuration)
            case "P" if current_page > 1:
                response = get_animals(token, current_page - 1, find_configuration)
            case "E":
                break
            case _:
                print("Invalid option. Try again!")


def get_animals(token, page_number, find_configuration):
    # Here we need to transform a configuration dictionary into a query parameter string
    # We do so in two steps:
    # -- 1 - We create a list of strings as such: {a: 1, b: 2} -> ["&a=1", "&b=2"]
    # -- 2 - We join all of the string values as such: "&a=1&b=2"
    config_params_list = [f"&{k}={v}" for k, v in find_configuration.items()]
    config_params = "".join(config_params_list)

    try:
        return requests.get(
            f"{common.API_URL}/animals?page={page_number}{config_params}",
            headers={"Authorization": f"Bearer {token}"},
        ).json()
    except requests.RequestException:
        sys.exit("Request to get animals failed.")


def tabulate_animals(animals, favourited_animals):
    formatted_animals = [
        format_animal(animal, favourited_animals) for animal in animals
    ]

    return tabulate(
        [
            [
                "ID",
                "Type",
                "Breed",
                "Color",
                "Age",
                "Gender",
                "Size",
                "Adoptable",
                "Location",
                "URL",
                "Favourited",
            ],
            *formatted_animals,
        ],
        headers="firstrow",
        tablefmt="rounded_outline",
        showindex="always",
    )


def format_animal(animal, favourited_animals):
    color = animal["colors"]["primary"]
    status = animal["status"]
    city = animal["contact"]["address"]["city"]
    state = animal["contact"]["address"]["state"]

    return [
        animal["type"],
        animal["breeds"]["primary"],
        color if color != None else "Unknown",
        animal["age"],
        animal["gender"],
        animal["size"],
        "Yes" if status == "adoptable" else "No",
        f"{city}, {state}",
        common.hide_url(animal["url"]),
        "Yes" if animal["id"] in favourited_animals else "No",
    ]
