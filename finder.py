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
    try:
        response = requests.get(
            f"{common.API_URL}/animals",
            headers={"Authorization": f"Bearer {token}"},
        ).json()
    except requests.RequestException:
        sys.exit("Request failed.")

    while True:
        num_total_animals = response["pagination"]["total_count"]
        num_page_animals = len(response["animals"])
        current_page = response["pagination"]["current_page"]
        total_pages = response["pagination"]["total_pages"]

        print(f"Found {num_total_animals} pets.")

        animals_table = tabulate_animals(response["animals"])
        print(animals_table)

        print(find_menu(num_page_animals, current_page, total_pages))

        match input("Choose option: ").upper():
            case num if str(num).isdigit() and 0 <= int(num) < num_page_animals:
                print("NUM")
            case "N":
                print("NEXT")
            case "P":
                print("PREVIOUS")
            case "E":
                break
            case _:
                print("Invalid option. Try again!")


def tabulate_animals(animals):
    formatted_animals = list(map(format_animal, animals))

    return tabulate(
        [
            [
                "ID",
                "Species",
                "Breed",
                "Color",
                "Age",
                "Gender",
                "Size",
                "Adoptable",
                "URL",
                #"Favourited"
            ],
            *formatted_animals,
        ],
        headers="firstrow",
        tablefmt="rounded_outline",
        showindex="always",
    )


def format_animal(animal):
    color = animal["colors"]["primary"]
    status = animal["status"]

    return [
        animal["type"],
        animal["breeds"]["primary"],
        color if color != None else "Unknown",
        animal["age"],
        animal["gender"],
        animal["size"],
        "Yes" if status == "adoptable" else "No",
        common.hide_url(animal["url"]),
    ]
