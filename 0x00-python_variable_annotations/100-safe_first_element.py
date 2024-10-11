#!/usr/bin/env python3

"""
Annotation
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    A function that returns any type of data or none
    """
    if lst:
        return lst[0]
    else:
        return None
