#!/usr/bin/env python3
"""7-to_kv.py"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ type-annotated function to return a tuple """
    tuple = (k, float(v ** 2))
    return tuple
