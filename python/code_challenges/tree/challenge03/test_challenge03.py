import pytest
from challenge03 import inOrderTraversal, arrayToBST, TreeNode

def test_empty_array():
    """
    Test case for an empty array input to sortedArrayToBST.
    """
    sortedArray = []
    tree = arrayToBST(sortedArray)
    values_in_order = []
    inOrderTraversal(tree, values_in_order)
    assert values_in_order == []

def test_single_element():
    """
    Test case for a single element array input to sortedArrayToBST.
    """
    sortedArray = [5]
    tree = arrayToBST(sortedArray)
    values_in_order = []
    inOrderTraversal(tree, values_in_order)
    assert values_in_order == [5]

def test_two_elements():
    """
    Test case for a two elements array input to sortedArrayToBST.
    """
    sortedArray = [2, 3]
    tree = arrayToBST(sortedArray)
    values_in_order = []
    inOrderTraversal(tree, values_in_order)
    assert values_in_order == [2, 3]

def test_even_elements():
    """
    Test case for an even number of elements array input to sortedArrayToBST.
    """
    sortedArray = [1, 2, 3, 4]
    tree = arrayToBST(sortedArray)
    values_in_order = []
    inOrderTraversal(tree, values_in_order)
    assert values_in_order == [1, 2, 3, 4]

def test_normal_case():
    """
    Test case for a normal sorted array input to sortedArrayToBST.
    """
    sortedArray = [0, 1, 2, 3, 4, 5]
    tree = arrayToBST(sortedArray)
    values_in_order = []
    inOrderTraversal(tree, values_in_order)
    assert values_in_order == [0, 1, 2, 3, 4, 5]