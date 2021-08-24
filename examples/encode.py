#!/usr/bin/env python
# coding:utf-8
"""
Name    : encode.py
Author  : Matias Selser
Time    : 8/24/21 8:55 AM
Desc    : Simple app that encodes an input string using an input encoding method into a file
"""

from os import path

import myparser.encoding as encoding

if __name__ == "__main__":

    data_path = "./data/"

    print("Please enter output file name:")
    file_name = input()

    file_path = data_path + file_name

    if path.exists(file_path):
        raise Exception("File already exists")

    print("Please enter encoding:")
    encoding_type = input()

    if encoding_type not in encoding.ENCODING:
        raise Exception(
            "Wrong encoding parameter. Should be: Should be  utf_32, utf_32_be, utf_32_le, utf_16,"
            " utf_16_be, utf_16_le, utf_7, utf_8 or utf_8_sig"
        )

    print("Please enter string to encode:")
    str_to_encode = input()

    with open(file_path, "wb") as f:
        f.write(str_to_encode.encode(encoding_type))
        f.close()
