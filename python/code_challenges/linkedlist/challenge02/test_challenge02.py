# Write your test here
import pytest
from challenge02 import LinkedList

def test_find_middle_empty_list():
    ll = LinkedList()
    assert ll.find_middle() == "List is Empty"

def test_find_middle_single_element():
    ll = LinkedList()
    ll.append(1)
    assert ll.find_middle() == "List only contain one or two element/s"

def test_find_middle_two_elements():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    assert ll.find_middle() == "List only contain one or two element/s"

def test_find_middle_odd_number_of_elements():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.find_middle() == 2

def test_find_middle_even_number_of_elements():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    assert ll.find_middle() == 3

def test_find_middle_larger_odd_list():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    assert ll.find_middle() == 3

def test_find_middle_larger_even_list():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    assert ll.find_middle() == 4

