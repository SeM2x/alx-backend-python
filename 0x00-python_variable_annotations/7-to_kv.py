#!/usr/bin/env python3
"""module defining to_kv function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    """function that returns a tuple"""
    return (k, v * v)
