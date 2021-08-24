#!/usr/bin/env python
# coding:utf-8
"""
Library that compares performance between substring finding functions
"""

import os
import random
import string
import time

import matplotlib.pyplot as plt


def measure_performance(encoding, min_substring_len, times_to_avg, len_list, functions):
    """Function that given an encoding, a minimum substring length, the number of times to get an average value,
    the string length iterator, and the functions to compare measures the time required to find the substrings

    :param encoding: Encoding method
    :type encoding: str
    :param min_substring_len: Minimum substring length in characters
    :type min_substring_len: int
    :param times_to_avg: Number of times to get average
    :type times_to_avg: int
    :param len_list: List of string length values
    :type len_list: list
    :param functions: List of functions to test
    :type functions: list
    """

    time_dict = {}
    for str_times in len_list:
        with open("test.txt", "wb") as f:
            aux_str = ""
            for _ in range(str_times):
                aux_str += random.choice(string.ascii_lowercase)
            f.write(aux_str.encode(encoding))
            f.close()

            for function in functions:
                aux = []
                for _ in range(times_to_avg):
                    with open("test.txt", "rb") as f:
                        time_start = time.perf_counter()
                        function(f, encoding, min_substring_len)
                        time_elapsed = time.perf_counter() - time_start
                    aux.append(time_elapsed)
                try:
                    time_dict[function.__name__].append(sum(aux) / len(aux))
                except KeyError:
                    time_dict[function.__name__] = [sum(aux) / len(aux)]

        os.remove("test.txt")

    plt.style.use("seaborn-darkgrid")
    for name, time_elapsed in time_dict.items():
        plt.plot(len_list, time_elapsed, label=name)
    plt.legend()
    plt.xlabel("String length [characters]")
    plt.ylabel("Time [seconds]")
    plt.show()
