import menu.finder as finder


def test_find_menu():
    assert finder.find_menu(20, 1, 50) == (
        "╭──────┬───────────────────────────────────────╮\n"
        "│ ID   │ Option                                │\n"
        "├──────┼───────────────────────────────────────┤\n"
        "│ 0-19 │ Select a pet to favourite/unfavourite │\n"
        "│ N    │ Next page of buddies (1/50)           │\n"
        "│ P    │ Previous page of buddies (1/50)       │\n"
        "│ E    │ Exit to menu                          │\n"
        "╰──────┴───────────────────────────────────────╯"
    )

    assert finder.find_menu(10, 20, 100) == (
        "╭──────┬───────────────────────────────────────╮\n"
        "│ ID   │ Option                                │\n"
        "├──────┼───────────────────────────────────────┤\n"
        "│ 0-9  │ Select a pet to favourite/unfavourite │\n"
        "│ N    │ Next page of buddies (20/100)         │\n"
        "│ P    │ Previous page of buddies (20/100)     │\n"
        "│ E    │ Exit to menu                          │\n"
        "╰──────┴───────────────────────────────────────╯"
    )


def test_format_animal():
    animal = {
        "id": 65310160,
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

    formatted_animal = finder.format_animal(animal, [65310160])

    assert len(formatted_animal) == 10
    assert formatted_animal[-4] == "Yes"
    assert formatted_animal[-1] == "Yes"

    animal["status"] = "adopted"
    formatted_animal = finder.format_animal(animal, [11111111])

    assert len(formatted_animal) == 10
    assert formatted_animal[-1] == "No"
    assert formatted_animal[-4] == "No"
