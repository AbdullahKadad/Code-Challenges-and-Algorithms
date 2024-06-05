# Write your test here
import pytest
from challenge03 import Stack
from challenge03 import delete_middle_element
@pytest.fixture
def stack1():
    stack = Stack()
    elements = [1, 2, 3, 4]
    for elem in elements:
        stack.push(elem)
    return stack

@pytest.fixture
def stack2():
    stack = Stack()
    elements = [1, 2, 3, 4, 5]
    for elem in elements:
        stack.push(elem)
    return stack

def test_delete_middle_element_stack1(stack1):
    delete_middle_element(stack1)
    assert stack1.stack == [1, 3, 4], f"Expected [1, 3, 4] but got {stack1.stack}"

def test_delete_middle_element_stack2(stack2):
    delete_middle_element(stack2)
    assert stack2.stack == [1, 2, 4, 5], f"Expected [1, 2, 4, 5] but got {stack2.stack}"

def test_delete_middle_element_empty():
    stack = Stack()
    delete_middle_element(stack)
    assert stack.stack == [], f"Expected [] but got {stack.stack}"

def test_delete_middle_element_one_element():
    stack = Stack()
    stack.push(1)
    delete_middle_element(stack)
    assert stack.stack == [], f"Expected [] but got {stack.stack}"

def test_delete_middle_element_two_elements():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    delete_middle_element(stack)
    assert stack.stack == [2], f"Expected [2] but got {stack.stack}"
