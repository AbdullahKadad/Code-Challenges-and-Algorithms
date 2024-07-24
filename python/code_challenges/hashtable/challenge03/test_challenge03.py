import pytest
from challenge03 import sum_of_unique_elements

def test_empty_array():
    """
    Test that the function returns 0 for an empty array.
    """
    assert sum_of_unique_elements([]) == 0

def test_all_unique_elements():
    """
    Test that the function returns the sum of all elements when all are unique.
    """
    assert sum_of_unique_elements([1, 2, 3, 4, 5]) == 15

def test_no_unique_elements():
    """
    Test that the function returns 0 when no elements are unique.
    """
    assert sum_of_unique_elements([1, 1, 2, 2, 3, 3]) == 0

def test_some_unique_elements():
    """
    Test that the function returns the sum of elements that appear exactly once.
    """
    assert sum_of_unique_elements([1, 2, 2, 3, 4, 4, 5]) == 9

def test_one_element():
    """
    Test that the function returns the single element when the array has only one element.
    """
    assert sum_of_unique_elements([42]) == 42

def test_all_elements_same():
    """
    Test that the function returns 0 when all elements in the array are the same.
    """
    assert sum_of_unique_elements([7, 7, 7, 7, 7]) == 0

def test_large_array_with_repeating_patterns():
    """
    Test that the function correctly handles a large array with repeating patterns.
    """
    assert sum_of_unique_elements([1, 2, 3, 1, 2, 3, 4]) == 4

def test_negative_numbers():
    """
    Test that the function correctly handles negative numbers and finds unique ones.
    """
    assert sum_of_unique_elements([-1, -2, -3, -1, -2, -4]) == -7

def test_mixed_positive_and_negative_numbers():
    """
    Test that the function correctly handles a mix of positive and negative numbers.
    """
    assert sum_of_unique_elements([-1, 1, -2, 2, -3, 3, -1, 1, -2, 2]) == 0

def test_array_with_zero():
    """
    Test that the function correctly handles arrays that include zero.
    """
    assert sum_of_unique_elements([0, 1, 2, 0, 3, 2]) == 4
