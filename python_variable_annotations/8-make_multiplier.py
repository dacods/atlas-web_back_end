#!/usr/bin/env python3
"""
takes a float as argument and returns a
function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    "Returns multiplied float"
    def newFunction(n: float):
        return n * multiplier
    return newFunction
