#!/usr/bin/env python3
"""
1-simple_pagination
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Function that returns a tuple of the start index and the end
        index for those particular pagination parameters."""
    num_page = page - 1
    idx_start = num_page * page_size
    idx_end = page * page_size
    return (idx_start, idx_end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Method that takes two integer arguments page with default
            value 1 and page_size with default value 10."""
        idx = index_range(page, page_size)
        idx_start = idx[0]
        idx_end = idx[1]

        res = self.dataset()
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        list_pages = []
        try:
            for i in range(idx_start, idx_end):
                list_pages.append(res[i])
            return list_pages
        except IndexError:
            return []
