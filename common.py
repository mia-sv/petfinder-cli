API_URL = "https://api.petfinder.com/v2"
FAVOURITES_FILE = ".favourites"


# This only works for bash terminals
def hide_url(url):
    return f"\u001b]8;;{url}\u001b\\Click here!\u001b]8;;\u001b\\"


def save_favourites(new_favourites):
    file = open(FAVOURITES_FILE, "w")

    for favourite in set(new_favourites):
        file.write(f"{favourite}\n")

    file.close()


def get_favourites():
    try:
        file = open(FAVOURITES_FILE, "r")

        lines = file.readlines()
        file.close()

        return set([int(line[:-1]) for line in lines])
    except FileNotFoundError:
        return set()
