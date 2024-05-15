class Node:
    def __init__(self, data=None):
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

    def delete_node(self, node):
        """
        Deletes the given node from the linked list and returns it.

        Args:
            node (Node): The node to be deleted.

        Returns:
            Node: The deleted node.

        Raises:
            ValueError: If the node is None 
    """
        if not node:
            raise AttributeError("Node is None")

        next_node = node.next
        node.data = next_node.data
        node.next = next_node.next

        return str(self)

if __name__ == "__main__":

    my_linked_list = LinkedList()

    my_linked_list.append(1)
    my_linked_list.append(2)
    my_linked_list.append(3)

    print("Before deletion:")
    print(my_linked_list)

    node_to_delete = my_linked_list.head.next
    deleted_node = my_linked_list.delete_node(node_to_delete)

    print("After deletion:")
    print(my_linked_list)