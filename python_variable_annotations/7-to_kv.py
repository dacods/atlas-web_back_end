#!/usr/bin/env python3
"Function to conver string and int/float to tuple"
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    "Returns arguments as tuple"
    return  (k, v ** 2)
