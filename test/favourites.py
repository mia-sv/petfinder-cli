import menu.favourites as favourites


def test_format_animal():
    animal = {
        "url": "https://www.petfinder.com/dog/rosemary-65310160/mn/crystal/healing-hearts-rescue-inc-mn465/?referrer_id=f8a1eed9-0fb7-4c3b-b02f-634fc6bb2e7f",
        "type": "Dog",
        "breeds": {"primary": "Australian Cattle Dog / Blue Heeler"},
        "colors": {
            "primary": "None",
            "secondary": "None",
            "tertiary": "None",
        },
        "age": "Adult",
        "gender": "Female",
        "size": "Medium",
        "status": "adoptable",
        "contact": {"address": {"city": "Crystal", "state": "MN"}},
    }

    formatted_animal = favourites.format_animal(animal)

    assert len(formatted_animal) == 9
    assert formatted_animal[-3] == "Yes"

    animal["status"] = "adopted"

    formatted_animal = favourites.format_animal(animal)

    assert len(formatted_animal) == 9
    assert formatted_animal[-3] == "No"


def test_favourites_menu():
    assert favourites.favourites_menu(20) == (
        "╭──────┬──────────────────────────────╮\n"
        "│ ID   │ Option                       │\n"
        "├──────┼──────────────────────────────┤\n"
        "│ 0-19 │ Remove a pet from favourites │\n"
        "│ E    │ Exit to menu                 │\n"
        "╰──────┴──────────────────────────────╯"
    )

    assert favourites.favourites_menu(5) == (
        "╭──────┬──────────────────────────────╮\n"
        "│ ID   │ Option                       │\n"
        "├──────┼──────────────────────────────┤\n"
        "│ 0-4  │ Remove a pet from favourites │\n"
        "│ E    │ Exit to menu                 │\n"
        "╰──────┴──────────────────────────────╯"
    )


def test_get_animal_ids():
    animals = [
        {"id": 1, "other": 0},
        {"id": 2, "other": 0},
        {"id": 3, "other": 0},
        {"other": 0},
    ]

    assert favourites.get_animal_ids(animals) == [1, 2, 3]
