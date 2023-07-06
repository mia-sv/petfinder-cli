from tabulate import tabulate
from decouple import config
import sys
import requests

MAIN_MENU = tabulate(
    [
        ["ID", "Option"],
        ["1", "Find your forever buddy"],
        ["2", "Show your favourite soon-to-be buddies"],
        ["3", "Configure your buddy search preferences"],
        ["4", "Exit"],
    ],
    headers="firstrow",
    tablefmt="rounded_outline",
)

try:
    API_KEY = config("API_KEY")
    API_SECRET = config("API_SECRET")
except UndefinedValueError:
    sys.exit("Missing API key or secret.")

API_URL = "https://api.petfinder.com/v2"


def main():
    token = generate_token()

    while True:
        print(MAIN_MENU)

        match input("Choose option: "):
            case "1":
                find(token)
            case "2":
                favourite(token)
            case "3":
                configure()
            case "4":
                sys.exit(0)
            case _:
                print("Invalid option. Try again!")


# This only works for bash terminals
def hide_url(url):
    return f"\u001b]8;;{url}\u001b\\Click here!\u001b]8;;\u001b\\"


def find(token):
    def format_animal(animal):
        return [
            animal["id"],
            animal["type"],
            animal["breeds"]["primary"],
            animal["colors"]["primary"],
            animal["age"],
            animal["gender"],
            animal["size"],
            animal["status"],
            hide_url(animal["url"]),
        ]

    try:
        response = requests.get(
            f"{API_URL}/animals", headers={"Authorization": f"Bearer {token}"}
        ).json()
    except requests.RequestException:
        sys.exit("Request failed.")

    total_count = response["pagination"]["total_count"]
    current_page = response["pagination"]["current_page"]
    total_pages = response["pagination"]["total_pages"]

    animals = list(map(format_animal, response["animals"]))

    results_table = tabulate(
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
            ],
            *animals,
        ],
        headers="firstrow",
        tablefmt="rounded_outline",
    )

    print(results_table)


def favourite(token):
    print("Favourite")


def configure():
    print("Configure")


def generate_token():
    try:
        response = requests.post(
            f"{API_URL}/oauth2/token",
            data={
                "grant_type": "client_credentials",
                "client_id": API_KEY,
                "client_secret": API_SECRET,
            },
        )
    except requests.RequestException:
        print("Failed to get API token. Malformed request.")
        sys.exit(1)

    if response.status_code != 200:
        print("Failed to get API token. Check your credentials.")
        sys.exit(1)

    return response.json()["access_token"]


if __name__ == "__main__":
    main()
