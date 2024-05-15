# Write your test here
from challenge01 import Node, LinkedList

my_linked_list = LinkedList()

my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

def test_delete_node():
    actual = my_linked_list.delete_node(my_linked_list.head.next)
    expected = "1 -> 3 -> 4 -> 5"
    print(actual, expected)
    assert actual == expected

def test_delete_node_2():
    actual = my_linked_list.delete_node(my_linked_list.head.next.next)
    expected = "1 -> 3 -> 5"
    print(actual, expected)
    assert actual == expected

def test_delete_node_AttributeError():
    try:
        my_linked_list.delete_node(2)
    except Exception as e:
        actual = type(e)
    expected = AttributeError
    assert actual == expected