"""Testing the functions in dictionary.py."""

___author___ = "730556372"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest


# Invert tests
def test_invert_key_error() -> None:
    """Invert with value occurring more than once raises key error."""
    with pytest.raises(KeyError):
        my_dictionary = {'alyssa': 'byrnes', 'adam': 'byrnes'}
        invert(my_dictionary)


def test_invert_null_dictionary() -> None:
    """Invert works on an empty dictionary."""
    assert invert({}) == {}


def test_invert_country_and_beverage() -> None:
    """Invert works with a few country & beverage pairs."""
    assert invert({"France": "Champagne", "Russia": "Vodka", "Turkey": "Raki"}) == {"Champagne": "France", "Vodka": "Russia", "Raki": "Turkey"}


def test_invert_school_and_state() -> None:
    """Invert works for a long dictionary."""
    assert invert({"UCLA": "CA", "MIT": "MA", "UNC": "NC", "UMich": "MI", "UTA": "TX", "ASU": "AZ", "UVA": "VA"}) == {"CA": "UCLA", "MA": "MIT", "NC": "UNC", "MI": "UMich", "TX": "UTA", "AZ": "ASU", "VA": "UVA"}


def test_favorite_color_null_dictionary() -> None:
    """Favorite_color returns an empty string when given an empty dictionary."""
    assert favorite_color({}) == ""


def test_favorite_color_all_different() -> None:
    """Favorite_color returns the first color when all the favorite colors are different."""
    assert favorite_color({"Erik": "Red", "Roy": "Blue", "Iago": "Green", "James": "Brown"}) == "Red"


def test_favorite_color_some_pairs() -> None:
    """Favorite_color works for a long dictionary."""
    assert favorite_color({"Abigail": "Red", "Benjamin": "Yellow", "Chris": "Green", "Daniel": "Blue", "Evan": "Red", "Fiona": "Green", "George": "Blue", "Harry": "Red", "Ian": "Green", "Shrek": "Green"}) == "Green"


def test_count_null_list() -> None:
    """Count returns an empty dictionary when given an empty list."""
    assert count([]) == {}


def test_count_three_distinct_strings() -> None:
    """Count on a list of three distinct strings returns a dictionary in which each string is paired with 1."""
    assert count(["boot", "boots", "bootie"]) == {"boot": 1, "boots": 1, "bootie": 1}


def test_count_long_list() -> None:
    """Count on a long list works."""
    assert count(["python", "java", "c++", "c++", "python", "python", "java", "python", "c++"]) == {"python": 4, "java": 2, "c++": 3}


def test_alphabetizer_null_list() -> None:
    """Alphabetizer returns an empty dictionary when given an empty list."""
    assert alphabetizer([]) == {}


def test_alphabetizer_three_strings_with_different_first_letters() -> None:
    """Alphabetizer works with three strings with different first letters."""
    assert alphabetizer(["well", "dwell", "swell"]) == {"w": ["well"], "d": ["dwell"], "s": ["swell"]}


def test_alphabetizer_long_list_communist_manifesto() -> None:
    """Alphabetizer works with a long list."""
    assert alphabetizer(["A", "spectre", "is", "haunting", "Europe", "the", "spectre", "of", "communism", "All", "the", "powers", "of", "old", "Europe", "have", "entered", "into", "a", "holy", "alliance", "to", "exorcise", "this", "spectre", "Pope", "and", "Tsar", "Metternich", "and", "Guizot", "French", "Radicals", "and", "German", "police-spies"]) == {'a': ['A', 'All', 'a', 'alliance', 'and', 'and', 'and'], 's': ['spectre', 'spectre', 'spectre'], 'i': ['is', 'into'], 'h': ['haunting', 'have', 'holy'], 'e': ['Europe', 'Europe', 'entered', 'exorcise'], 't': ['the', 'the', 'to', 'this', 'Tsar'], 'o': ['of', 'of', 'old'], 'c': ['communism'], 'p': ['powers', 'Pope', 'police-spies'], 'm': ['Metternich'], 'g': ['Guizot', 'German'], 'f': ['French'], 'r': ['Radicals']}


def test_update_attendance_null_dictionary() -> None:
    """Update_attendance works with an empty dictionary."""
    assert update_attendance({}, "Monday", "Bernie") == {"Monday": ["Bernie"]}


def test_update_attendance_two_days() -> None:
    """Update_attendance works with two days given and another day the same as the first."""
    assert update_attendance({"Tuesday": ["Hillary", "Bernie"], "Thursday": ["Donald", "Ted"]}, "Thursday", "John") == {"Tuesday": ["Hillary", "Bernie"], "Thursday": ["Donald", "Ted", "John"]}


def test_update_attendance_new_day() -> None:
    """Update_attendance works with adding a new day flavored with world leader's first names."""
    assert update_attendance({"Monday": ["Boris", "Angela", "Emmanuel"], "Wednesday": ["Donald", "Justin"]}, "Friday", "Jinping") == {"Monday": ["Boris", "Angela", "Emmanuel"], "Wednesday": ["Donald", "Justin"], "Friday": ["Jinping"]}


def test_update_attendance_repeat_student1() -> None:
    """Update_attendance works with multiple people with the same name."""
    assert update_attendance({"Saturday": ["Joe"]}, "Saturday", "Joe") == {"Saturday": ["Joe"]}