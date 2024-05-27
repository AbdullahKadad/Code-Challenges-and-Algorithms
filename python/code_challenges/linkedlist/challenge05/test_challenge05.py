# Write your test here
import pytest
from challenge05 import LinkedList

def test_append():
    list = LinkedList()
    list.append(1)
    list.append(2)
    list.append(3)
    list.append(4)
    list.append(5)
    assert str(list) == "1 -> 2 -> 3 -> 4 -> 5"

def test_insert_after():
    list = LinkedList()
    list.append(1)
    list.append(2)
    list.append(3)
    list.append(4)
    list.append(5)

    list.insert_after(1, 1.5)
    assert str(list) == "1 -> 1.5 -> 2 -> 3 -> 4 -> 5"

    list.insert_after(1.5, 1.75)
    assert str(list) == "1 -> 1.5 -> 1.75 -> 2 -> 3 -> 4 -> 5"

    list.insert_after(5, 6)
    assert str(list) == "1 -> 1.5 -> 1.75 -> 2 -> 3 -> 4 -> 5 -> 6"

    list.insert_after(6, 7)
    assert str(list) == "1 -> 1.5 -> 1.75 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7"

def test_insert_after_nonexistent_value():
    list = LinkedList()
    list.append(1)
    list.append(2)
    list.append(3)

    with pytest.raises(ValueError, match="Value 4 not found in the list"):
        list.insert_after(4, 4.5)



