from tabulate import tabulate
from decouple import config
import sys
import requests

from menu.finder import find as find
from menu.favourites import favourites as favourites
from menu.configure import configure as configure
import common


def main():
    api_key, api_secret = get_config()

    token = generate_token(api_key, api_secret)

    while True:
        print_menu()

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


def generate_token(api_key, api_secret):
    try:
        response = requests.post(
            f"{common.API_URL}/oauth2/token",
            data={
                "grant_type": "client_credentials",
                "client_id": api_key,
                "client_secret": api_secret,
            },
        )
    except requests.RequestException:
        print("Failed to get API token. Malformed request.")
        sys.exit(1)

    if response.status_code != 200:
        print("Failed to get API token. Check your credentials.")
        sys.exit(1)

    return response.json()["access_token"]


def print_menu():
    print(
        tabulate(
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
    )


def get_config():
    try:
        return config("API_KEY"), config("API_SECRET")
    except UndefinedValueError:
        sys.exit("Missing API key or secret.")


if __name__ == "__main__":
    main()
