#!/usr/bin/env python3
"""Type-annotated function sum_list"""
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """[Function that takes a list input_list of floats as
        argument and returns their sum as a float]

        Args:
            input_list (list): [list of floats]

        Returns:
            float: [it's the sum of floats]
        """
    return sum(input_list)
