#!/usr/bin/env python3
from typing import List


def sum_list(input_list: list[float]) -> float:
    """ type-annotated function to return their sum as a float """
    sum = 0
    for number in input_list:
        sum += number
    return sum
