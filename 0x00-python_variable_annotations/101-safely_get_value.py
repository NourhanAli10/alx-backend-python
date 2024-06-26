#!/usr/bin/env python3
"""101-safely_get_value.py"""
from typing import Any, Sequence, Union, TypeVar, Mapping


T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ type-annotated function with the correct duck-typed annotations"""
    if key in dct:
        return dct[key]
    else:
        return default
