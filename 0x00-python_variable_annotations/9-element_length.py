#!/usr/bin/env python3

"""
Annotation of function parameters
"""

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    A complex annotation function
    """
    return [(i, len(i)) for i in lst]
