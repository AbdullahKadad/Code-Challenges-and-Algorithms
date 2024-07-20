import pytest
from challenge01 import TreeNode, find_pair_with_sum

@pytest.fixture
def bst():
    """
    Creates a binary search tree (BST) with the following structure:
    """
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(20)
    return root

@pytest.fixture
def bst_with_duplicates():
    """
    Creates a BST with duplicate values and the following structure:
    """
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(20)
    return root

@pytest.fixture
def empty_bst():
    """
    Creates an empty BST.
    """
    return None

@pytest.fixture
def bst_single_node():
    """
    Creates a BST with a single node.
    """
    return TreeNode(10)

def test_find_pair_with_sum_found(bst):
    """
    Tests that find_pair_with_sum returns True when there exists a pair of nodes
    that sum to the target value.
    """
    assert find_pair_with_sum(bst, 22) == True
    assert find_pair_with_sum(bst, 17) == True
    assert find_pair_with_sum(bst, 25) == True

def test_find_pair_with_sum_not_found(bst):
    """
    Tests that find_pair_with_sum returns False when there does not exist a pair of nodes
    that sum to the target value.
    """
    assert find_pair_with_sum(bst, 18) == False
    assert find_pair_with_sum(bst, 40) == False

def test_find_pair_with_sum_empty_tree(empty_bst):
    """
    Tests that find_pair_with_sum returns False when the tree is empty.
    """
    assert find_pair_with_sum(empty_bst, 10) == False

def test_find_pair_with_sum_single_node(bst_single_node):
    """
    Tests that find_pair_with_sum returns False when the tree has only a single node.
    """
    assert find_pair_with_sum(bst_single_node, 20) == False

def test_find_pair_with_sum_duplicates(bst_with_duplicates):
    """
    Tests that find_pair_with_sum correctly handles trees with duplicate values.
    """
    assert find_pair_with_sum(bst_with_duplicates, 10) == True
    assert find_pair_with_sum(bst_with_duplicates, 7) == True
