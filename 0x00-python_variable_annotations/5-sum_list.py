#!/usr/bin/env python3
from typing import List
""" define fn sum_list """


def sum_list(input_list: List[float]) -> float:
    """
    type-annotated function sum_list
    takes a list input_list of floats as argument
    and returns their sum as a float.
    """
    s: float = 0.0
    for el in input_list:
        s += el
    return s
