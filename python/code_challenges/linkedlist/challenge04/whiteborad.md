# Linked List Implementation with Reverse Function

This repository contains a Python implementation of a singly linked list with the ability to reverse the list in place.

## Classes

### `Node`

A class representing a node in a singly linked list.

**Attributes:**

- `data`: The data stored in the node.
- `next (Node)`: The next node in the linked list.

**Methods:**

- `__init__(self, data=None)`: Initializes a new node with the given data. The default value for data is `None`.

### `LinkedList`

A class representing a singly linked list.

**Attributes:**

- `head (Node)`: The head node of the linked list.

**Methods:**

- `__init__(self)`: Initializes an empty linked list.
- `append(self, data)`: Appends a new node with the given data to the end of the linked list.
- `__str__(self)`: Converts the linked list to a string representation and returns it.
- `reverse_list(self)`: Reverses the linked list in place.

## White Board

![White Board](./List%20(1).jpg)

![Step Through](./List%20(2).jpg)
