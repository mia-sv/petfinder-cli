API_URL = "https://api.petfinder.com/v2"
FAVOURITES_FILE = ".favourites"


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
