API_URL = "https://api.petfinder.com/v2"
FAVOURITES_FILE = ".favourites"
CONFIGURATION_FILE = ".configuration"


# This only works for bash terminals
def hide_url(url):
    return f"\u001b]8;;{url}\u001b\\Click here!\u001b]8;;\u001b\\"


def save_favourites_to_file(favourites):
    file = open(FAVOURITES_FILE, "w")

    for fav in set(favourites):
        file.write(f"{fav}\n")

    file.close()


def get_favourites_from_file():
    try:
        file = open(FAVOURITES_FILE, "r")

        lines = file.readlines()
        file.close()

        # We remove the (\n) and convert to int
        return set([int(line[:-1]) for line in lines])
    except FileNotFoundError:
        return set()


def save_configuration_to_file(configuration):
    file = open(CONFIGURATION_FILE, "w")

    for k, v in configuration.items():
        file.write(f"{k}:{v}\n")

    file.close()


def get_configuration_from_file():
    try:
        file = open(CONFIGURATION_FILE, "r")

        lines = file.readlines()
        file.close()

        configuration = {}

        for line in lines:
            config_pair = line.split(":")

            if len(config_pair) == 2:
                key = config_pair[0].strip()
                value = config_pair[1].strip()

                configuration[key] = value

        # We remove the (\n) and convert to int
        return configuration
    except FileNotFoundError:
        return {}


# Checks if val is an int and between a (inclusive) and b (exclusive)
def is_int_and_between(val, a, b):
    return str(val).isdigit() and a <= int(val) < len(b)


# Joins primary, secondary and tertiary animal colors
def get_animal_colors(colors_dict):
    colors_list = [
        colors_dict.get("primary"),
        colors_dict.get("secondary"),
        colors_dict.get("tertiary"),
    ]

    return ", ".join([c for c in colors_list if c != None and c != "None"])
