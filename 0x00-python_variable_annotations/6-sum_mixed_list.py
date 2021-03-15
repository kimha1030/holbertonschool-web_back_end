#!/usr/bin/env python3
"""Type-annotated function sum_mixed_list"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """[Function that takes a list mxd_lst of integers and floats and it
        returns their sum as a float]

        Args:
            mxd_lst (list): [list of integers and floats]

        Returns:
            float: [it's the sum of floats]
        """
    return sum(mxd_lst)
