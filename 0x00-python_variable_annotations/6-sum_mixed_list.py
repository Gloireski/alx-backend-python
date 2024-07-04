#!/usr/bin/env python3
"""
define sum_mixed_list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    type-annotated function sum_mixed_list
    """
    s: float = 0.0
    for el in mxd_lst:
        s += el
    return s
