"""EX06 - Making a dictionary? I wasn't told what the doc string should be."""

__author__ = "730556372"


def invert(initial_dictionary: dict[str, str]) -> dict[str, str]:
    """Swapping keys and values in a dictionary."""
    new_dictionary: dict[str, str] = {}  # New dictionary that will swap the keys and values
    for key in initial_dictionary:
        value: str = initial_dictionary[key]  # Making a swapped key-value pair
        if value in new_dictionary:
            raise KeyError(f"{value} appears too many times in the dictionary to invert it")  # Checking for repeated values
        new_dictionary[value] = key
    return new_dictionary


def favorite_color(colors: dict[str, str]) -> str:
    """Finding a favorite color."""
    if len(colors) == 0:
        return ""
    colors_list: list[str] = []  # Getting a list of the colors that appear
    for name in colors:
        color: str = colors[name]
        if color not in colors_list:
            colors_list.append(color)
    # Initializing a list of the colors occurring most frequently and the most common frequency
    most_common_colors: list[str] = []
    max_color_frequency: int = 0
    # Looping through colors to see how frequent they are and then updating most_common_colors and max_color_frequency accordingly
    for color in colors_list:
        color_frequency: int = 0
        for name in colors:
            if color == colors[name]:
                color_frequency += 1
        if color_frequency == max_color_frequency:
            most_common_colors.append(color)
        if color_frequency > max_color_frequency:
            max_color_frequency = color_frequency
            most_common_colors = [color]
    return most_common_colors[0]


def count(a_bunch_of_strings: list[str]) -> dict[str, int]:
    """Counting how many time each string appears in the list."""
    idx: int = 0  # Generating the dictionary one string at a time
    list_length: int = len(a_bunch_of_strings)
    frequencies: dict[str, int] = {}
    while idx < list_length:
        a_string: str = a_bunch_of_strings[idx]
        if a_string in frequencies:
            frequencies[a_string] += 1  # Updating the value for a_string if it already appeared
        else:
            frequencies[a_string] = 1  # Initializing the value for a_string
        idx += 1
    return frequencies


def alphabetizer(strings_to_sort: list[str]) -> dict[str, list[str]]:
    """Finding the initial letters of the strings and then grouping the strings by that letter."""
    idx: int = 0  # Generating the dictionary one string at a time based on the first letter
    list_length: int = len(strings_to_sort)
    alphabetized: dict[str, list[str]] = {}
    while idx < list_length:
        current_string: str = strings_to_sort[idx]
        lower_case_string: str = current_string.lower()
        first_letter: str = lower_case_string[0]
        if first_letter in alphabetized:
            alphabetized[first_letter].append(current_string)
        else:
            alphabetized[first_letter] = [current_string]
        idx += 1
    return alphabetized


def update_attendance(attendance_log: dict[str, list[str]], week_day: str, student: str) -> dict[str, list[str]]:
    """Updating attendance."""
    if week_day in attendance_log:  # Either adding the student to the week day or adding a pair of the week day and the student
        if student not in attendance_log[week_day]:
            attendance_log[week_day].append(student)
    else:
        attendance_log[week_day] = [student]
    return attendance_log