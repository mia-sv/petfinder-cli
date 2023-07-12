from tabulate import tabulate
import requests

import common


def favourites(token):
    favourited_animals_ids = common.get_favourites_from_file()

    # Fetch favourites 1 by 1 from the API, by id
    print("Fetching favourite animal info...", end="", flush=True)
    animals = [get_animal(token, id) for id in favourited_animals_ids]
    print()

    # Filter our every single animal whose request failed
    # and remove them from the file
    animals = [animal for animal in animals if animal != None]
    common.save_favourites_to_file(get_animal_ids(animals))

    while True:
        print(tabulate_animals(animals))
        print(favourites_menu(len(animals)))

        match input("Choose option: ").upper():
            case num if common.is_int_and_between(num, 0, len(animals)):
                # Fetches the id from the animal at the index we enter.
                animal_id = animals[int(num)]["id"]

                # Updates the list of animals by removing the animal with matching id
                animals = [animal for animal in animals if animal["id"] != animal_id]

                # Updates the favourites file with the new list (without the matching id)
                common.save_favourites_to_file(get_animal_ids(animals))
            case "E":
                break
            case _:
                print("Invalid option. Try again!")


def get_animal(token, id):
    try:
        response = requests.get(
            f"{common.API_URL}/animals/{id}",
            headers={"Authorization": f"Bearer {token}"},
        ).json()

        print(".", end="", flush=True)

        # If a request for animal fails,
        # we assume that it does not exist.
        if "animal" in response:
            return response["animal"]
        else:
            return None
    except requests.RequestException:
        sys.exit("Request to get animal failed.")


def format_animal(animal):
    color = common.get_animal_colors(animal["colors"])
    status = animal["status"]
    city = animal["contact"]["address"]["city"]
    state = animal["contact"]["address"]["state"]

    return [
        animal["type"],
        animal["breeds"]["primary"],
        color if color else "Unknown",
        animal["age"],
        animal["gender"],
        animal["size"],
        "Yes" if status == "adoptable" else "No",
        f"{city}, {state}",
        common.hide_url(animal["url"]),
    ]


def tabulate_animals(animals):
    formatted_animals = [format_animal(animal) for animal in animals]

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
                "Location",
                "URL",
            ],
            *formatted_animals,
        ],
        headers="firstrow",
        tablefmt="rounded_outline",
        showindex="always",
    )


def favourites_menu(pet_count):
    return tabulate(
        [
            ["ID", "Option"],
            [f"0-{pet_count  - 1}", "Remove a pet from favourites"],
            ["E", "Exit to menu"],
        ],
        headers="firstrow",
        tablefmt="rounded_outline",
    )


def get_animal_ids(animals):
    return [animal["id"] for animal in animals if "id" in animal]
