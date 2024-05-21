# Write your test here
import pytest 
from challenge03 import LinkedList

@pytest.fixture
def setup_linkedlist():
    """
    Fixture to set up a linked list for testing.
    """
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    return ll

def test_append(setup_linkedlist):
    """
    Test the append method of LinkedList.
    """
    ll = setup_linkedlist
    assert str(ll) == '1 -> 2 -> 3 -> 4 -> 5'

def test_remove_node_end(setup_linkedlist):
    """
    Test the remove_node_end method of LinkedList.
    """
    ll = setup_linkedlist
    ll.remove_node_end(2)
    assert str(ll) == '1 -> 2 -> 3 -> 5'

def test_remove_only_node():
    """
    Test removing the only node in the list.
    """
    ll = LinkedList()
    ll.append(1)
    ll.remove_node_end(1)
    assert str(ll) == ''

def test_remove_head_node():
    """
    Test removing the head node.
    """
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.remove_node_end(2)
    assert str(ll) == '2'

def test_remove_tail_node():
    """
    Test removing the tail node in a list of two nodes.
    """
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.remove_node_end(1)
    assert str(ll) == '1'
