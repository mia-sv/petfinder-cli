#  PetFinder CLI

### Introduction
Petfinder is an online database of animals who are searching for their forever home, as well as a directory of shelters and animal orgaizations across the USA, Mexico and Canada.

Petfinder CLI is a command line searcher for pets, using the Petfinder API, allowing users to search, configure and save the information about the animals available on the website.

This program was submmited as the [CS50P](https://cs50.harvard.edu/python/2022/) final project.

### Features
- Searching all animals available on Petfinder, informing the users which ones are still adoptable and where, as well as their phisical characteristics.
- Configuring searches, allowing users to search for a pet with specific characteristics at a specific location.
- Bookmarking pets as favourites, so users can track them and their current state.
- All configuration and favourite pets' data is persisted.

  Video Demo: [Click Here.](https://raw.githubusercontent.com/mia-sv/petfinder-cli/main/Video%20Presentation.mp4)

### Running Instructions
1. Create an account on Petfinder and generate an API key and secret and put them in `.env`.
2. Install all of the pip requirements in `requirements.txt`.
3. Run `python project.py` in your terminal.

### Project Structure 
- The `menu` package consists of all the files that implement the necessary functionalities for the program's features: `finder.py`, `favourites.py` and `configure.py`, called by the project.py file.
- The `test` package contains `pytest` test files for all of the functionalities in `menu` package. These files are called in the `test_project.py` file and have the same names as their counterparts in the `menu` package.
- The `common.py` file gathers all of the functions and constants which are shared through multiple files.
