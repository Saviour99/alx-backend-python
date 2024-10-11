#!/usr/bin/env python3

"""
Advance annotations
"""

from typing import Tuple, List, Any


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> List:
    """
    A function that duplicates elements in a tuple based
    on the factor.

    Args:
        lst (Tuple[Any, ...]): The input tuple.
        factor (int, optional): The number of times to duplicate
        each element. Defaults to 2.

    Returns:
        List[Any]: The resulting list with duplicated elements.
    """
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in

# Change the array to a tuple for type consistency
array = (12, 72, 91)  # Changed to tuple

zoom_2x = zoom_array(array)  # Using the original array

zoom_3x = zoom_array(array, 3)  # Corrected factor to int
