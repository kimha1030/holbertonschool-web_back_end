#!/usr/bin/env python3
"""Type-annotated function make_multiplier"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """[Function that takes a float multiplier as argument and returns a
        function that multiplies a float by multiplier]

        Args:
            multiplier (float): [float used in operation]

        Returns:
            float: [Function that multiplies a float by multiplier]
        """
    return lambda x: multiplier*x
