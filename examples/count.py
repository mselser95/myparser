#!/usr/bin/env python
# coding:utf-8
"""
Name    : count.py
Author  : Matias Selser
Time    : 8/23/21 12:36 PM
Desc    : Simple app that given a file, encoding method and min substring length, counts the substrings
"""

import myparser.argparser as argparser
import myparser.stringparser as stringparser

if __name__ == "__main__":

    decoding_args = argparser.get_args()

    if argparser.validate_args(decoding_args):
        f = open(decoding_args.file, "rb")
        substrings = stringparser.get_substrings_repetitions_dict(
            file_to_decode=f,
            encoding=decoding_args.encoding,
            min_substring_len=decoding_args.minlen,
        )
        if substrings:
            print(substrings)
        else:
            print("No substrings found!")
