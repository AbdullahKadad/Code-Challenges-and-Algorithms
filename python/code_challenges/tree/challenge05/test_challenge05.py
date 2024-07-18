# Write your test here
import pytest
from challenge05 import TreeNode, max_height

@pytest.fixture
def tree1():
    """
    Fixture for the following tree:
        1
       / \
      2   3
     / \
    4   5
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root

@pytest.fixture
def tree2():
    """
    Fixture for the following tree:
        1
         \
          2
           \
            3
    """
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    return root

@pytest.fixture
def tree3():
    """
    Fixture for an empty tree.
    """
    return None

def test_max_height_tree1(tree1):
    assert max_height(tree1) == 2

def test_max_height_tree2(tree2):
    assert max_height(tree2) == 2

def test_max_height_tree3(tree3):
    assert max_height(tree3) == -1
