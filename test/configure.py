import menu.configure as configure


def test_keys_menu():
    keys_list = sorted(list(configure.PARAMETERS.keys()))

    configuration = {
        "age": "senior",
        "color": "white",
        "gender": "female",
        "type": "cat",
        "location": "Los Angeles, CA",
    }

    assert configure.keys_menu(configuration, keys_list) == (
        "╭──────┬─────────────────┬─────────────────╮\n"
        "│ ID   │ Option          │ Current Value   │\n"
        "├──────┼─────────────────┼─────────────────┤\n"
        "│ 0    │ Change Age      │ Senior          │\n"
        "│ 1    │ Change Color    │ White           │\n"
        "│ 2    │ Change Gender   │ Female          │\n"
        "│ 3    │ Change Type     │ Cat             │\n"
        "│ L    │ Change Location │ Los Angeles, CA │\n"
        "│ E    │ Exit to menu    │                 │\n"
        "╰──────┴─────────────────┴─────────────────╯"
    )


def test_values_menu():
    values_list = ["blue", "white", "red", "black", "purple", "lilac"]

    assert configure.values_menu(values_list) == (
        "╭──────┬───────────╮\n"
        "│ ID   │ Option    │\n"
        "├──────┼───────────┤\n"
        "│ 0    │ Blue      │\n"
        "│ 1    │ White     │\n"
        "│ 2    │ Red       │\n"
        "│ 3    │ Black     │\n"
        "│ 4    │ Purple    │\n"
        "│ 5    │ Lilac     │\n"
        "│ A    │ Any value │\n"
        "╰──────┴───────────╯"
    )
