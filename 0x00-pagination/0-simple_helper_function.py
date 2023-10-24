#!/usr/bin/env python3
"""Simple helper function -that takes two integer arguments page and page_size
"""


def index_range(page, page_size):
    """return a tuple of size two containing a start index and an end index
       corresponding to the range of indexes to return in a list for
       those particular pagination parameters.
    """
    if page and page_size:
        index_start = (page - 1) * page_size
        index_end = index_start + page_size
        return index_start, index_end
