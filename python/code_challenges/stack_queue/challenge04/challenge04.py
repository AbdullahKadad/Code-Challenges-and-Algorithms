# Write here the code challenge solution
class Queue:
    """
    A simple implementation of a queue using a list.
    
    Methods:
        is_empty() -> bool:
            Checks if the queue is empty.
            
        enqueue(item) -> None:
            Adds an item to the end of the queue.
            
        dequeue() -> any:
            Removes and returns the item from the front of the queue. 
            Raises IndexError if the queue is empty.
            
        size() -> int:
            Returns the number of items in the queue.
            
        __repr__() -> str:
            Returns a string representation of the queue.
    """
    
    def __init__(self):
        """Initializes an empty queue."""
        self.items = []

    def is_empty(self):
        """Checks if the queue is empty."""
        return len(self.items) == 0

    def enqueue(self, item):
        """Adds an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """
        Removes and returns the item from the front of the queue.
        Raises IndexError if the queue is empty.
        """
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("dequeue from an empty queue")

    def size(self):
        """Returns the number of items in the queue."""
        return len(self.items)

    def __repr__(self):
        """Returns a string representation of the queue."""
        return f"Queue({self.items})"

def reverse_queue(queue):
    """
    Reverses the order of elements in a given queue.
    
    Args:
        queue (Queue): The queue to be reversed.
        
    Returns:
        Queue: The queue with the elements in reversed order.
    """
    stack = []
    
    # Dequeue all elements from the queue and push them onto the stack
    while not queue.is_empty():
        stack.append(queue.dequeue())
    
    # Pop all elements from the stack and enqueue them back into the queue
    while stack:
        queue.enqueue(stack.pop())
    
    return queue


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    
    print("Original Queue:", q)
    reversed_q = reverse_queue(q)
    print("Reversed Queue:", reversed_q)
