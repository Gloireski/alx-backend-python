#!/usr/bin/env python3
"""
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union [int, float]) -> Tuple:
    """
     type-annotated function to_kv
    """
    return (k, v ** 2)
