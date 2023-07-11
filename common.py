API_URL = "https://api.petfinder.com/v2"
FAVOURITES_FILE = ".favourites"

CONFIGURATION = {}


# This only works for bash terminals
def hide_url(url):
    return f"\u001b]8;;{url}\u001b\\Click here!\u001b]8;;\u001b\\"


def save_strset_to_file(items, filename):
    file = open(filename, "w")

    for item in set(items):
        file.write(f"{item}\n")

    file.close()


def get_intset_from_file(filename):
    try:
        file = open(filename, "r")

        lines = file.readlines()
        file.close()

        # We remove the (\n) and convert to int
        return set([int(line[:-1]) for line in lines])
    except FileNotFoundError:
        return set()


# Checks if val is an int and between a (inclusive) and b (exclusive)
def is_int_and_between(val, a, b):
    return str(val).isdigit() and a <= int(val) < len(b)
