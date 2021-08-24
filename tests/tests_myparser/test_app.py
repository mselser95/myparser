#!/usr/bin/env python
# coding:utf-8
"""
Name    : test_app.py
Author  : Matias Selser
Time    : 8/23/21 3:08 PM
Desc    :
"""
import pytest

testdata = [1, 1, 1]


@pytest.mark.parametrize("a", testdata)
def test_app(a):
    assert a == 1
