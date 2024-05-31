# Write your test here
import pytest
from challenge01 import MyQueue

@pytest.fixture
def my_queue():
    return MyQueue()


def test_myqueue(my_queue):
    # Test push and peek
    my_queue.push(1)
    my_queue.push(2)
    assert my_queue.peek() == 1

    # Test pop
    assert my_queue.pop() == 1
    assert my_queue.peek() == 2
    assert not my_queue.empty()

    # Test pop and empty
    assert my_queue.pop() == 2
    assert my_queue.empty()
