# Write here the code challenge solution
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
    
    def reverse_list(self):
        """
        Reverses the linked list in place.
        """
        original = self.head
        reverse = None
        while original:
            savior = original.next
            original.next = reverse
            reverse = original
            original = savior
        self.head = reverse 

if __name__ == "__main__":
    
    list = LinkedList()
    list.append(1)
    list.append(2)
    list.append(3)
    list.append(4)
    list.append(5)

    print("Original list:")
    print(list)

    list.reverse_list()
    print("Reversed list:")
    print(list)

    list.reverse_list()
    print("Reversed list 2 (original List):")
    print(list)