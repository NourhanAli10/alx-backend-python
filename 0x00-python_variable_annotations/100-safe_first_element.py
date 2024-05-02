#!/usr/bin/env python3
"""100-safe_first_element.py"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ type-annotated function with the correct duck-typed annotations"""
    if lst:
        return lst[0]
    else:
        return None
