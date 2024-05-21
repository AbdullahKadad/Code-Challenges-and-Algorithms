class Node:
    """
    A class representing a node in a singly linked list.

    Attributes:
        data: The data stored in the node.
        next (Node): The next node in the linked list.
    """
    def __init__(self, data=None):
        """
        Initializes a new node with the given data.

        Args:
            data: The data to be stored in the node. Default is None.
        """
        self.data = data
        self.next = None

class LinkedList:
    """
    A class representing a singly linked list.

    Attributes:
        head (Node): The head node of the linked list.
    """
    def __init__(self):
        """
        Initializes an empty linked list.
        """
        self.head = None

    def append(self, data):
        """
        Appends a new node with the given data to the end of the linked list.

        Args:
            data: The data to be stored in the new node.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def remove_node_end(self, index):
        """
        Removes the node at the given index from the end of the linked list.

        Args:
            index (int): The index from the end of the node to be removed.

        Returns:
            str: A string representation of the linked list after removal.
        """
        dummy = Node(0)
        dummy.next = self.head
        pointer_1 = dummy
        pointer_2 = dummy

        # Advance pointer_1 by index steps
        for _ in range(index):
            if not pointer_1.next:  # If index is larger than the length of the list
                return str(self)
            pointer_1 = pointer_1.next

        # Move both pointers until pointer_1 reaches the end
        while pointer_1.next:
            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.next

        # Remove the node
        pointer_2.next = pointer_2.next.next

        # Update the head in case the head node was removed
        self.head = dummy.next

        return str(self)
    
    def __str__(self):
        """
        Converts the linked list to a string representation.

        Returns:
            str: A string representation of the linked list.
        """
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return ' -> '.join(elements)

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)

    print("Original List:")
    print(ll)

    ll.remove_node_end(2)
    print("After removing 2nd node from end:")
    print(ll)

    
    ll2 = LinkedList()
    ll2.append(1)
    print("Original List with one node:")
    print(ll2)
    ll2.remove_node_end(1)  # Removing the only node in the list
    print("After removing the only node:")
    print(ll2)

    ll3 = LinkedList()
    ll3.append(1)
    ll3.append(2)
    print("Original List with two nodes:")
    print(ll3)
    ll3.remove_node_end(2)  # Removing the head node
    print("After removing the head node:")
    print(ll3)

    ll4 = LinkedList()
    ll4.append(1)
    ll4.append(2)
    print("Original List with two nodes:")
    print(ll4)
    ll4.remove_node_end(1)  # Removing the tail node in a list of two nodes
    print("After removing the tail node in a list of two nodes:")
    print(ll4)
