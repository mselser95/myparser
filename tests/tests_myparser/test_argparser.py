#!/usr/bin/env python
# coding:utf-8
"""
Name    : test_argparser.py
Author  : Matias Selser
Time    : 8/24/21 10:08 AM
Desc    :
"""

import pytest

import myparser.argparser as argparser


class TestObject:
    def __init__(self, encoding, minlen, file):
        self.encoding = encoding
        self.minlen = minlen
        self.file = file


arguments = [
    (
        TestObject(encoding="invalid encoding", minlen=2, file="file_that_exists.txt"),
        Exception("Encoding parameter incorrect, please check input"),
    ),
    (
        TestObject(encoding="utf_8", minlen=0, file="file_that_exists.txt"),
        Exception("minlen parameter incorrect, please check input"),
    ),
    (
        TestObject(encoding="utf_8", minlen=2, file="file_that_doesnt_exists.txt"),
        Exception("file parameter incorrect, please check if file exists"),
    ),
]


@pytest.mark.parametrize("arguments,output", arguments)
def test_validate_args(arguments, output):

    with pytest.raises(Exception) as excinfo:
        argparser.validate_args(arguments)
    assert str(excinfo.value) == str(output)
