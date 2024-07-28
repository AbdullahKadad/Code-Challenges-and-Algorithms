import pytest
from challenge04 import reorder_people_by_height

def test_no_people():
    """
    Test that the function returns an empty list when there are no people.
    """
    assert reorder_people_by_height([], []) == []

def test_single_person():
    """
    Test that the function returns the single person when there is only one person.
    """
    assert reorder_people_by_height(["Alice"], [155]) == ["Alice"]

def test_two_people():
    """
    Test that the function correctly orders two people by height.
    """
    assert reorder_people_by_height(["Bob", "Alice"], [185, 155]) == ["Bob", "Alice"]

def test_people_with_unique_heights():
    """
    Test that the function correctly orders multiple people with unique heights.
    """
    assert reorder_people_by_height(["Alice", "Bob", "Charlie"], [155, 185, 200]) == ["Charlie", "Bob", "Alice"]

def test_people_with_duplicate_heights():
    """
    Test that the function correctly handles multiple people with the same height.
    """
    assert reorder_people_by_height(["Alice", "Bob", "Charlie"], [155, 185, 185]) == ["Bob", "Charlie", "Alice"]

def test_large_group_of_people():
    """
    Test that the function correctly handles a large group of people with mixed heights.
    """
    names = ["Person1", "Person2", "Person3", "Person4", "Person5"]
    heights = [160, 180, 150, 170, 175]
    expected_order = ["Person2", "Person5", "Person4", "Person1", "Person3"]
    assert reorder_people_by_height(names, heights) == expected_order



