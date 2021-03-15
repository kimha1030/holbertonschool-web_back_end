#!/usr/bin/env python3
"""Type-annotated function safely_get_value"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')
unionTNone = Union[T, None]
unionAnyT = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: unionTNone = None) -> unionAnyT:
    """ Function safely_get_value"""
    if key in dct:
        return dct[key]
    else:
        return default
