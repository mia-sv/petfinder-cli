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

API_KEY = config("API_KEY")
API_SECRET = config("API_SECRET")
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


def find(token):
    try:
        find_animals = requests.get(
            f"{API_URL}/animals", headers={"Authorization": f"Bearer {token}"}
        ).json()
    except requests.RequestException:
        sys.exit("Request failed.")

    print(find_animals)


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


# user_input = input("What's your favorite pet?\n[1]Dog [2]Cat [3]Other\n")
