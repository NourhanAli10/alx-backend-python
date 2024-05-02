#!/usr/bin/env python3
"""6-sum_mixed_list.py"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ type-annotated function to return their sum as a float """
    sum = 0
    for number in mxd_lst:
        sum += number
    return float(sum)
