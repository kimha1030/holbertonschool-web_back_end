#!/usr/bin/env python3
"""Type-annotated function to_kv"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """[Function that takes a string k and an int OR float v as
        arguments and returns a tuple]

        Args:
            k (str): [string used in tuple]
            v (int or float): [integer or float used in tuple]

        Returns:
            float: [tuple, where first element is string  and second
            element is the square of integer o float]
        """
    return (k, v*v)
