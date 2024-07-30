import pytest
from challenge05 import find_intersection

def test_find_intersection_basic():
    arr1 = ["1", "2", "2", "1"]
    arr2 = [2, 2]
    assert sorted(find_intersection(arr1, arr2)) == [2]

def test_find_intersection_mixed_types():
    arr1 = [1, 2, 2, 1]
    arr2 = ["2", "1"]
    result = find_intersection(arr1, arr2)
    assert sorted(result) == [1, 2]

def test_find_intersection_no_intersection():
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert find_intersection(arr1, arr2) == []

def test_find_intersection_duplicates_in_both():
    arr1 = [1, 2, 2, 1]
    arr2 = [2, 1, 2]
    result = find_intersection(arr1, arr2)
    assert sorted(result) == [1, 2]

def test_find_intersection_empty_first_array():
    arr1 = []
    arr2 = [1, 2, 3]
    assert find_intersection(arr1, arr2) == []

def test_find_intersection_empty_second_array():
    arr1 = [1, 2, 3]
    arr2 = []
    assert find_intersection(arr1, arr2) == []

def test_find_intersection_both_empty():
    arr1 = []
    arr2 = []
    assert find_intersection(arr1, arr2) == []

def test_find_intersection_repeated_elements():
    arr1 = [1, 1, 1, 1]
    arr2 = [1, 1]
    assert find_intersection(arr1, arr2) == [1]

def test_find_intersection_all_elements_match():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [5, 4, 3, 2, 1]
    result = find_intersection(arr1, arr2)
    assert sorted(result) == [1, 2, 3, 4, 5]