#!/usr/bin/env python3
"""
definir fnc make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    type-annotated function make_multiplier
    """
    return lambda y: multiplier * y
