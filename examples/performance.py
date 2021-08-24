#!/usr/bin/env python
# coding:utf-8
"""
Name    : performance.py
Author  : Matias Selser
Time    : 8/24/21 9:13 AM
Desc    :
"""

import myparser.performance as performance
import myparser.stringparser as stringparser

if __name__ == "__main__":
    functions = [
        stringparser.get_substrings_repetitions_set,
        stringparser.get_substrings_repetitions_dict,
    ]
    performance.measure_performance(
        encoding="utf_8",
        min_substring_len=2,
        times_to_avg=10,
        len_list=[x for x in range(100, 1000, 100)],
        functions=functions,
    )
