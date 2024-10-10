#!/usr/bin/env python3
"""module defining element_length function"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function that returns a list of tuples"""
    return [(i, len(i)) for i in lst]
