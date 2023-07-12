import test.common as common
import test.finder as finder
import test.favourites as favourites
import test.configure as configure


def test_common():
    common.test_is_int_and_between()
    common.test_get_animal_colors()
    common.test_hide_url()


def test_finder():
    finder.test_find_menu()
    finder.test_format_animal()


def test_favourites():
    favourites.test_format_animal()
    favourites.test_favourites_menu()
    favourites.test_get_animal_ids()


def test_configure():
    configure.test_values_menu()
    configure.test_keys_menu()
