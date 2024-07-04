#!/usr/bin/env python3
"""
define fn element_length
"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    function element_length
    """
    return [(i, len(i)) for i in lst]
