#!/usr/bin/env python3
"""8-make_multiplier.py"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ type-annotated function to return function
    that multiplies a float by multiplier """
    def multiple(x: float) -> float:
        return float(x * multiplier)
    return multiple
