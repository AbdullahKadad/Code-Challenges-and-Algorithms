class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self.stack = []

    def push(self, item):
        """Add an item to the top of the stack.
        
        Args:
            item: The item to be added to the stack.
        """
        self.stack.append(item)

    def pop(self):
        """Remove and return the item from the top of the stack.
        
        Returns:
            The item from the top of the stack if the stack is not empty, otherwise None.
        """
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        """Check if the stack is empty.
        
        Returns:
            True if the stack is empty, False otherwise.
        """
        return len(self.stack) == 0

    def size(self):
        """Return the number of elements in the stack.
        
        Returns:
            The number of elements in the stack.
        """
        return len(self.stack)

    def __repr__(self):
        """Return a string representation of the stack.
        
        Returns:
            A string representing the stack.
        """
        return repr(self.stack)

def delete_middle_element(stack):
    """
    Delete the middle element of the stack. If the stack has an even number of elements, 
    it removes the element at index n/2 (0-based index).
    
    Args:
        stack (Stack): The stack from which the middle element will be deleted.
    """
    def delete_recursively(stack, current_index, middle_index):
        """
        Helper function to delete the middle element using recursion.
        
        Args:
            stack (Stack): The stack from which the middle element will be deleted.
            current_index (int): The current index being processed.
            middle_index (int): The index of the middle element.
        """
        if stack.is_empty():
            return
        top = stack.pop()
        if current_index != middle_index:
            delete_recursively(stack, current_index + 1, middle_index)
            stack.push(top)

    if stack.is_empty():
        return
    middle_index = stack.size() // 2
    delete_recursively(stack, 0, middle_index)

if __name__ == "__main__":

    stack1 = Stack()
    elements1 = [1, 2, 3, 4]
    for elem in elements1:
        stack1.push(elem)

    print(f"Original stack: {stack1}")
    delete_middle_element(stack1)
    print(f"Stack after deleting middle element: {stack1}")

    stack2 = Stack()
    elements2 = [1, 2, 3, 4, 5]
    for elem in elements2:
        stack2.push(elem)

    print(f"Original stack: {stack2}")
    delete_middle_element(stack2)
    print(f"Stack after deleting middle element: {stack2}")