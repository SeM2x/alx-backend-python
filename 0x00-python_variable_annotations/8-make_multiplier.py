#!/usr/bin/env python3
"""module defining make_multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function that returns a function that multiplies a float by multiplier"""
    def multiply(n: float) -> float:
        """function that multiplies a float by multiplier"""
        return multiplier * n
    return multiply
