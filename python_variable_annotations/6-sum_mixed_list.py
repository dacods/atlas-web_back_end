#!/usr/bin/env python3
"Takes a list of integers and floats and returns their sum as a float."
from typing import Union, List


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    "returns sum of mixed list as float"
    return sum(mxd_list)
