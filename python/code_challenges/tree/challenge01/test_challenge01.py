import pytest
from challenge01 import Tree, Node, construct_tree

@pytest.fixture
def setup_tree():
    """
    Fixture to set up a Tree instance for testing.
    """
    return Tree()

def test_tree_empty(setup_tree):
    """
    Test case for an empty tree.
    """
    tree = setup_tree
    assert str(tree) == "[]"

def test_construct_single_node(setup_tree):
    """
    Test case for constructing a tree with a single node.
    """
    tree = setup_tree
    preorder = [1]
    inorder = [1]
    tree.root = construct_tree(preorder, inorder).root
    assert str(tree) == "[1]"

def test_construct_normal_tree(setup_tree):
    """
    Test case for constructing a normal binary tree.
    """
    tree = setup_tree
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    tree.root = construct_tree(preorder, inorder).root
    assert str(tree) == "[3, 9, 20, None, None, 15, 7]"
