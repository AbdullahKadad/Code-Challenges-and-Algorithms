# Write your test here
import pytest
from challenge04 import LinkedList

@pytest.fixture
def linked_list():
    """
    Fixture to create and return a linked list with 5 nodes.
    """
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    return ll

def test_append(linked_list):
    """
    Test appending elements to the linked list.
    """
    assert str(linked_list) == "1 -> 2 -> 3 -> 4 -> 5"

def test_reverse_list(linked_list):
    """
    Test reversing the linked list.
    """
    linked_list.reverse_list()
    assert str(linked_list) == "5 -> 4 -> 3 -> 2 -> 1"
    linked_list.reverse_list()
    assert str(linked_list) == "1 -> 2 -> 3 -> 4 -> 5"

