import pytest
from challenge02 import are_trees_identical, Node, Tree, create_tree

# Test cases
def test_identical_trees():
    # case 1: Identical trees
    p1 = create_tree([1, 2, 3])
    q1 = create_tree([1, 2, 3])
    assert are_trees_identical(p1, q1) == True

    # case 2: One tree has None in place of a node
    p2 = create_tree([1, 2])
    q2 = create_tree([1, None, 2])
    assert are_trees_identical(p2, q2) == False

    # case 3: Different structure and values
    p3 = create_tree([1, 2, 1])
    q3 = create_tree([1, 1, 2])
    assert are_trees_identical(p3, q3) == False

    # case 4: Empty trees
    p4 = None
    q4 = None
    assert are_trees_identical(p4, q4) == True

    # case 5: Different values but same structure
    p5 = create_tree([1, 2, 3])
    q5 = create_tree([1, 3, 2])
    assert are_trees_identical(p5, q5) == False

    # case 6: Large trees with different values
    p6 = create_tree([1, 2, 3, 4, 5, 6, 7])
    q6 = create_tree([1, 2, 3, 4, 5, 6, 8])
    assert are_trees_identical(p6, q6) == False

    # case 7: Large trees with same values
    p7 = create_tree([1, 2, 3, 4, 5, 6, 7])
    q7 = create_tree([1, 2, 3, 4, 5, 6, 7])
    assert are_trees_identical(p7, q7) == True

