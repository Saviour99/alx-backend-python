#!/usr/bin/env python3

"""
Advance annotations
"""

from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any, default: Union[T, None] = None
        ) -> Union[Any, T]:
    """
    A funtion that returns a dict value or default
    """
    if key in dct:
        return dct[key]
    else:
        return default
