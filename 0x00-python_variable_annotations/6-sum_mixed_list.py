#!/usr/bin/env python3
"""module defining sum_mixed_list function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """function that returns the sum of the list of floats"""
    return sum(mxd_lst)
