from tabulate import tabulate

import common

PARAMETERS = {
    "age": ["baby", "young", "adult", "senior"],
    "color": [
        "black",
        "gray",
        "brown",
        "golden",
        "orange",
        "white",
    ],
    "gender": ["male", "female"],
    "type": ["dog", "cat"],
}


def keys_menu(configuration, keys_list):
    keys_list_formatted = [
        [
            idx,
            f"Change {key.capitalize()}",
            configuration.get(key, "Any").capitalize(),
        ]
        for idx, key in enumerate(keys_list)
    ]

    return tabulate(
        [
            ["ID", "Option", "Current Value"],
            *keys_list_formatted,
            ["L", "Change Location", configuration.get("location", "Any")],
            ["E", "Exit to menu", ""],
        ],
        headers="firstrow",
        tablefmt="rounded_outline",
    )


def values_menu(values_list):
    values_list_formatted = [v.capitalize() for v in values_list]
    values_list_formatted = list(enumerate(values_list_formatted))

    return tabulate(
        [
            ["ID", "Option"],
            *values_list_formatted,
            ["A", "Any value"],
        ],
        headers="firstrow",
        tablefmt="rounded_outline",
    )


def configure():
    configuration = common.get_configuration_from_file()

    keys_list = sorted(list(PARAMETERS.keys()))

    while True:
        print(keys_menu(configuration, keys_list))

        match input("Choose option: ").upper():
            case num if common.is_int_and_between(num, 0, keys_list):
                # num is the index of the key we choose from keys_list
                chosen_key = keys_list[int(num)]
                values_list = sorted(list(PARAMETERS[chosen_key]))

                configure_submenu(configuration, values_list, chosen_key)
            case "L":
                while True:
                    location_input = (
                        input(
                            "Insert location (City, State (2-letter)) or nothing: "
                        )
                        .replace("\n", "")
                        .lower()
                        .strip()
                    )

                    if len(location_input) == 0:
                        configuration.pop("location", None)
                        common.save_configuration_to_file(configuration)
                        break

                    location_pair = location_input.split(", ")

                    if len(location_pair) == 2 and len(location_pair[1]) == 2:
                        configuration[
                            "location"
                        ] = f"{location_pair[0].capitalize()}, {location_pair[1].upper()}"

                        common.save_configuration_to_file(configuration)

                        break
                    else:
                        print("Invalid location format.")
            case "E":
                break
            case _:
                print("Invalid option. Try again!")


def configure_submenu(configuration, values_list, chosen_key):
    while True:
        print(values_menu(values_list))

        match input("Choose option: ").upper():
            case num if common.is_int_and_between(num, 0, values_list):
                # num is the index of the key we choose from values_list
                chosen_value = values_list[int(num)]

                # Update the configuration with a new value
                configuration[chosen_key] = chosen_value
                common.save_configuration_to_file(configuration)
                break
            case "A":
                # Remove this key from the configuration
                configuration.pop(chosen_key, None)
                common.save_configuration_to_file(configuration)
                break
            case _:
                print("Invalid option. Try again!")
