#!/usr/bin/env python3
"""module defining safe_first_element function"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """function that returns the first element of a list"""
    if lst:
        return lst[0]
    else:
        return None
