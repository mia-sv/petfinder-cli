import common


def test_is_int_and_between():
    assert common.is_int_and_between(1, 0, 20) == True
    assert common.is_int_and_between(-1, 0, 20) == False
    assert common.is_int_and_between(1, 5, 20) == False
    assert common.is_int_and_between("hello", 5, 20) == False


def test_get_animal_colors():
    assert (
        common.get_animal_colors(
            {"primary": "Brown", "secondary": "White", "tertiary": "Black"}
        )
        == "Brown, White, Black"
    )
    assert common.get_animal_colors({"primary": "Brown"}) == "Brown"
    assert (
        common.get_animal_colors(
            {"primary": "None", "secondary": "None", "tertiary": "None"}
        )
        == ""
    )


def test_hide_url():
    assert (
        common.hide_url("https://www.google.com")
        == "\x1b]8;;https://www.google.com\x1b\\Click here!\x1b]8;;\x1b\\"
    )

    assert (
        common.hide_url("https://www.github.com")
        == "\x1b]8;;https://www.github.com\x1b\\Click here!\x1b]8;;\x1b\\"
    )
