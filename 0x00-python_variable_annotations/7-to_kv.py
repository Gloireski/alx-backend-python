#!/usr/bin/env python3
"""
define to_kv
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
     type-annotated function to_kv
    """
    x = v ** 2
    return (k, x)
