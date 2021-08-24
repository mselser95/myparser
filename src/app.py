#!/usr/bin/env python
# coding:utf-8
"""
Name    : app.py
Author  : Matias Selser
Time    : 8/23/21 12:36 PM
Desc    :
"""

import myparser.argparser as argparser
import myparser.stringparser as stringparser

if __name__ == "__main__":

    decoding_args = argparser.get_args()

    if argparser.validate_args(decoding_args):
        f = open(decoding_args.file, "rb")
        substrings = stringparser.get_substrings_repetitions(
            file_to_decode=f,
            bytes_length=decoding_args.len,
            min_substring_len=decoding_args.minlen,
        )
        if substrings:
            # print(substrings)
            pass
        else:
            print("No substrings found!")
