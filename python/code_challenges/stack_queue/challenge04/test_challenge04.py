# Write your test here
import pytest
from challenge04 import Queue, reverse_queue  

@pytest.fixture
def empty_queue():
    """Fixture for an empty queue."""
    return Queue()

@pytest.fixture
def single_element_queue():
    """Fixture for a queue with a single element."""
    q = Queue()
    q.enqueue(1)
    return q

@pytest.fixture
def multiple_elements_queue():
    """Fixture for a queue with multiple elements."""
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    return q

def test_reverse_empty_queue(empty_queue):
    """Test reversing an empty queue."""
    reversed_q = reverse_queue(empty_queue)
    assert reversed_q.is_empty()

def test_reverse_single_element_queue(single_element_queue):
    """Test reversing a queue with a single element."""
    reversed_q = reverse_queue(single_element_queue)
    assert reversed_q.size() == 1
    assert reversed_q.dequeue() == 1

def test_reverse_multiple_elements_queue(multiple_elements_queue):
    """Test reversing a queue with multiple elements."""
    reversed_q = reverse_queue(multiple_elements_queue)
    assert reversed_q.size() == 4
    assert reversed_q.dequeue() == 4
    assert reversed_q.dequeue() == 3
    assert reversed_q.dequeue() == 2
    assert reversed_q.dequeue() == 1
