# !/usr/bin/env python
# coding:utf-8
"""
Library that gets substrings repetition using parameters
"""


def get_substrings_repetitions_dict(file_to_decode, encoding, min_substring_len):
    """Function that parses a UTF-X file to find substrings repeated more than once, with a length greater than
    the minimum substring size parameter using a dictionary

    :param file_to_decode: File to decode
    :type file_to_decode: file
    :param encoding: Encoding method
    :type encoding: str
    :param min_substring_len: Minimum substring length in characters
    :type min_substring_len: int
    :return: Dictionary with the substring as key and the number of occurrences as value
    :rtype: dict
    """
    # Convert the whole file to a string format
    file_str = file_to_decode.read().decode(encoding)

    substrings = {}

    substrings_gen = (
        file_str[i:j]
        for i in range(0, len(file_str) - min_substring_len)
        for j in range(i + min_substring_len + 1, len(file_str) + 1)
    )

    for substring in substrings_gen:
        try:
            substrings[substring] += 1
        except KeyError:  # We create the key
            substrings[substring] = 1
    substrings = {key: substrings[key] for key in substrings if substrings[key] > 1}
    return substrings


def get_substrings_repetitions_set(file_to_decode, encoding, min_substring_len):
    """Function that parses a UTF-X file to find substrings repeated more than once, with a length greater than
    the minimum substring size parameter using a set

    :param file_to_decode: File to decode
    :type file_to_decode: file
    :param encoding: Encoding method
    :type encoding: str
    :param min_substring_len: Minimum substring length in characters
    :type min_substring_len: int
    :return: Dictionary with the substring as key and the number of occurrences as value
    :rtype: dict
    """
    # Convert the whole file to a string format
    file_str = file_to_decode.read().decode(encoding, errors="replace")

    substrings = {}
    substrings_gen = (
        file_str[i:j]
        for i in range(0, len(file_str) - min_substring_len)
        for j in range(i + min_substring_len + 1, len(file_str) + 1)
    )

    sub_set = set()
    len_sub_set = 0
    for substring in substrings_gen:
        sub_set.add(substring)
        new_subset_len = len(sub_set)
        if len_sub_set == new_subset_len:
            substrings[substring] += 1
        else:
            substrings[substring] = 1
        len_sub_set = new_subset_len

    substrings = {key: substrings[key] for key in substrings if substrings[key] > 1}

    return substrings
