#!/usr/bin/env python
# coding:utf-8
"""
Name    : test_stringparser.py
Author  : Matias Selser
Time    : 8/24/21 10:44 AM
Desc    :
"""

import os

import pytest

import myparser.stringparser as stringparser

encoding = [
    "utf_32",
    "utf_32_be",
    "utf_32_le",
    "utf_16",
    "utf_16_be",
    "utf_16_le",
    "utf_7",
    "utf_8",
    "utf_8_sig",
]


@pytest.mark.parametrize("encoding", encoding)
def test_get_substrings_repetitions_set(encoding):
    # given...
    test_str = "HoaHoaHoa"

    # Save encoded string to file
    with open("test.txt", "wb") as f:
        f.write(test_str.encode(encoding))
        f.close()
    min_len = 2

    # when...
    substrings = stringparser.get_substrings_repetitions_set(
        file_to_decode=open("test.txt", "rb"),
        encoding=encoding,
        min_substring_len=min_len,
    )

    # then...

    # Remove created file
    if os.path.exists("test.txt"):
        os.remove("test.txt")

    correct_output = {
        "Hoa": 3,
        "HoaH": 2,
        "HoaHo": 2,
        "HoaHoa": 2,
        "oaH": 2,
        "oaHo": 2,
        "oaHoa": 2,
        "aHo": 2,
        "aHoa": 2,
    }

    assert substrings == correct_output


@pytest.mark.parametrize("encoding", encoding)
def test_get_substrings_repetitions_dict(encoding):
    # given...
    test_str = "HoaHoaHoa"

    # Save encoded string to file
    with open("test.txt", "wb") as f:
        f.write(test_str.encode(encoding))
        f.close()
    min_len = 2

    # when...
    substrings = stringparser.get_substrings_repetitions_set(
        file_to_decode=open("test.txt", "rb"),
        encoding=encoding,
        min_substring_len=min_len,
    )

    # then...

    # Remove created file
    if os.path.exists("test.txt"):
        os.remove("test.txt")

    correct_output = {
        "Hoa": 3,
        "HoaH": 2,
        "HoaHo": 2,
        "HoaHoa": 2,
        "oaH": 2,
        "oaHo": 2,
        "oaHoa": 2,
        "aHo": 2,
        "aHoa": 2,
    }

    assert substrings == correct_output
