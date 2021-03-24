#!/usr/bin/env python3
"""
0. Simple helper function
"""
import typing


def index_range(page: int, page_size: int) -> typing.Tuple[int, int]:
    """ Function that returns a tuple of the start index and the end
        index for those particular pagination parameters."""
    num_page = page - 1
    idx_start = num_page * page_size
    idx_end = page * page_size
    return (idx_start, idx_end)
