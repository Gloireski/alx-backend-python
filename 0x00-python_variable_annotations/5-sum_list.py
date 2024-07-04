#!/usr/bin/env python3
""" define fn sum_list """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    type-annotated function sum_list
    """
    s: float = 0.0
    for el in input_list:
        s += el
    return s
