#!/usr/bin/env python3

"""
Advance annotations
"""

from typing import Tuple, List, Any, Union


def zoom_array(lst: List[Any], factor: Union[int, float] = 2) -> List[Any]:
    """
    A function that duplicates elements in a tuple based
    on the factor.

    Returns:
        List[Any]: The resulting list with duplicated elements.
    """
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
