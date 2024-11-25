#!/usr/bin/env python3

from not_none_functions import return_not_none

def test_return_not_none():
    '''Test that the function return_not_none returns None.'''
    result = return_not_none()
    assert result is None, f"Expected None, but got {result}"

