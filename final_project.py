from tabulate import tabulate
from decouple import config
import sys
import requests

from finder import find
from favourites import favourites
import common

MAIN_MENU = tabulate(
    [
        ["ID", "Option"],
        ["F", "Find your forever buddy"],
        ["S", "Show your favourite soon-to-be buddies"],
        ["C", "Configure your buddy search preferences"],
        ["Q", "Quit program."],
    ],
    headers="firstrow",
    tablefmt="rounded_outline",
)

try:
    API_KEY = config("API_KEY")
    API_SECRET = config("API_SECRET")
except UndefinedValueError:
    sys.exit("Missing API key or secret.")


def main():
    token = generate_token()

    while True:
        print(MAIN_MENU)

        match input("Choose option: ").upper():
            case "F":
                find(token)
            case "S":
                favourites(token)
            case "C":
                configure()
            case "Q":
                sys.exit(0)
            case _:
                print("Invalid option. Try again!")


def configure():
    print("Configure")


def generate_token():
    try:
        response = requests.post(
            f"{common.API_URL}/oauth2/token",
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
