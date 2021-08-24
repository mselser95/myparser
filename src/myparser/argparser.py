# !/usr/bin/env python
# coding:utf-8
"""
Name    : argparser.py
Author  : Matias Selser
Time    : 7/29/21 5:12 PM
Desc    : Library that gets and processes the arguments given by the user
"""

import argparse
from os import path


def get_args():
    """
    Function that reads the argument input. Returns the arguments
    :rtype: object
    """
    parser = argparse.ArgumentParser(
        description="Show and count substrings, "
        " which occur more than once and are longer than the optional"
        " length parameter. It should also work efficiently with large files."
    )

    parser.add_argument(
        "--file", type=str, required=True, help="Path to the file to process"
    )
    parser.add_argument(
        "--len",
        type=int,
        required=True,
        help="Number of bytes of the encoding (1 for UTF-8, 2"
        " for UTF-16, or 4 for UTF32)",
    )
    parser.add_argument(
        "--minlen",
        type=int,
        required=False,
        default=5,
        help="Minimum substring length to count",
    )

    args = parser.parse_args()
    return args


def validate_args(decoding_args):
    """
    Function that verifies if the arguments values are valid
    :rtype: bool
    """
    encoding = [1, 2, 4]
    if decoding_args.len <= 0 or decoding_args.len not in encoding:
        raise Exception("len parameter incorrect, please check input")

    if decoding_args.minlen <= 0:
        raise Exception("minlen parameter incorrect, please check input")

    if not path.exists(decoding_args.file):
        raise Exception("file parameter incorrect, please check if file exists")

    return True
