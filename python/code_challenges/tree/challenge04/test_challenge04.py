# Write your test here
import pytest
from challenge04 import TreeNode, find_max_value

@pytest.fixture
def sample_tree():
    """
    Create a sample binary tree for testing.
    """
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(20)
    return root

@pytest.fixture
def single_node_tree():
    """
    Create a single node tree for testing.
    """
    return TreeNode(42)

@pytest.fixture
def empty_tree():
    """
    Create an empty tree for testing.
    """
    return None

def test_find_max_value_in_sample_tree(sample_tree):
    assert find_max_value(sample_tree) == 20

def test_find_max_value_in_single_node_tree(single_node_tree):
    assert find_max_value(single_node_tree) == 42

def test_find_max_value_in_empty_tree(empty_tree):
    assert find_max_value(empty_tree) == "The tree is empty"
