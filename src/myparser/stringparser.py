# !/usr/bin/env python
# coding:utf-8
"""
Name    : stringparser.py
Author  : Matias Selser
Time    : 7/29/21 5:12 PM
Desc    : Library that process binary files
"""
import resource
import time

import matplotlib.pyplot as plt

UTF_8 = "utf-8"
UTF_16 = "utf-16-be"
UTF_32 = "utf-32-be"


def get_substrings_repetitions(file_to_decode, bytes_length, min_substring_len):
    """
    Funtion that parses a UTF-X file to find substrings repeated more than once, with a length greater than the minimum
    substring size parameter
    :param file_to_decode: File to decode
    :type file_to_decode: file
    :param bytes_length: Length of the character in bytes
    :type bytes_length: int
    :param min_substring_len: Minimum substring length in characters
    :type min_substring_len: int
    :return: Dictionary with the substring as key and the number of occurrences as value
    :rtype: dict


    """

    decoding = {
        1: UTF_8,
        2: UTF_16,
        4: UTF_32,
    }

    # Convert the whole file to a string format
    file_str = file_to_decode.read().decode(decoding[bytes_length], errors="replace")
    file_str = "HoaHoaHoa"

    first_time = []
    second_time = []
    first_mem = []
    second_mem = []
    str_len = []
    for k in range(10):
        str_len.append(len(file_str))
        time_1 = []
        time_2 = []
        mem_1 = []
        mem_2 = []
        for times in range(20):
            substrings = {}
            time_start = time.perf_counter()
            substrings_gen = (
                file_str[i:j]
                for i in range(0, len(file_str) - min_substring_len)
                for j in range(i + min_substring_len, len(file_str))
            )

            sub_set = set()
            len_sub_set = 0
            for substring in substrings_gen:
                sub_set.add(substring)
                nn = len(sub_set)
                if len_sub_set == nn:
                    substrings[substring] += 1
                else:
                    substrings[substring] = 1
                len_sub_set = nn

            substrings = {
                key: substrings[key] for key in substrings if substrings[key] > 1
            }
            time_elapsed = time.perf_counter() - time_start
            memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
            # print("%5.1f secs %5.1f MByte" % (time_elapsed, memMb))
            time_1.append(time_elapsed)
            mem_1.append(memMb)
            # print(substrings)

            time_start2 = time.perf_counter()
            substrings_gen = (
                file_str[i:j]
                for i in range(0, len(file_str) - min_substring_len)
                for j in range(i + min_substring_len, len(file_str))
            )
            substrings = {}

            for substring in substrings_gen:
                try:
                    substrings[substring] += 1
                except KeyError:  # We create the key
                    substrings[substring] = 1
            substrings = {
                key: substrings[key] for key in substrings if substrings[key] > 1
            }
            time_elapsed2 = time.perf_counter() - time_start2
            memMb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0 / 1024.0
            # print("%5.1f secs %5.1f MByte" % (time_elapsed2, memMb))
            # print(substrings)
            time_2.append(time_elapsed2)
            mem_2.append(memMb)

        first_time.append(sum(time_1) / len(time_1))
        second_time.append(sum(time_2) / len(time_2))
        first_mem.append(sum(mem_1) / len(mem_1))
        second_mem.append(sum(mem_2) / len(mem_2))

        file_str += "HoaHoaHoa"

    # print(time_1)
    # print(time_2)

    plt.subplot(2, 1, 1)
    plt.plot(str_len, first_time)
    plt.plot(str_len, second_time)
    plt.xlabel("String Length")
    plt.ylabel("Avg. Time")
    plt.subplot(2, 1, 2)
    plt.plot(str_len, first_mem)
    plt.plot(str_len, second_mem)
    plt.xlabel("String Length")
    plt.ylabel("Avg. Mem")
    plt.show()

    return substrings
