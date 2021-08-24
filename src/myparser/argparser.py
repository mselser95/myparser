# !/usr/bin/env python
# coding:utf-8
"""
Library that gets and processes the arguments given by the user
"""

import argparse
from os import path

import myparser.encoding as encoding


def get_args():
    """Function that reads the argument input. Returns the arguments

    :return: Object containing file path, encoding and min length
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
        "--encoding",
        type=str,
        required=True,
        help="Encoding. Should be  utf_32,"
        " utf_32_be,"
        " utf_32_le,"
        " utf_16,"
        " utf_16_be,"
        " utf_16_le,"
        " utf_7,"
        " utf_8 or"
        " utf_8_sig",
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
    """Function that verifies if the arguments values are valid

    :return: 'True' if ok else 'False'
    :rtype: bool
    """
    if decoding_args.encoding not in encoding.ENCODING:
        raise Exception("Encoding parameter incorrect, please check input")

    if decoding_args.minlen <= 0:
        raise Exception("minlen parameter incorrect, please check input")

    if not path.exists(decoding_args.file):
        raise Exception("file parameter incorrect, please check if file exists")

    return True
