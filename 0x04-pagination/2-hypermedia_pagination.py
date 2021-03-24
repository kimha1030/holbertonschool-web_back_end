import csv
import math
from typing import List, Dict


index_range = __import__('0-simple_helper_function').index_range


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
        list_pages = []
        idx = index_range(page, page_size)
        idx_start = idx[0]
        idx_end = idx[1]
        res = self.dataset()
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        try:
            for i in range(idx_start, idx_end):
                list_pages.append(res[i])
            return list_pages
        except IndexError:
            return list_pages

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ Method that takes the same arguments as get_page and
            returns a dictionary"""
        dict_pages = {}
        list_pages = self.get_page(page, page_size)
        len_pages = len(list_pages)
        res = self.dataset()
        total_pages = math.ceil(len(res) / page_size)
        if page is not 1:
            prev_page = page - 1
        else:
            prev_page = None
        if page < total_pages:
            next_page = page + 1
        else:
            next_page = None
        dict_pages["page_size"] = len_pages
        dict_pages["page"] = page
        dict_pages["data"] = list_pages
        dict_pages["next_page"] = next_page
        dict_pages["prev_page"] = prev_page
        dict_pages["total_pages"] = total_pages
        return dict_pages
