# Write here the code challenge solution
class MyQueue:
    """
    A queue implemented using two stacks.
    """

    def __init__(self):
        """
        Initialize two stacks.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of the queue.
        
        Args:
        x (int): Element to be pushed to the back of the queue.
        """
        self.stack1.append(x)

    def pop(self):
        """
        Removes the element from in front of the queue and returns that element.
        
        Returns:
        int: The element removed from the front of the queue.
        """
        self.peek()
        return self.stack2.pop()

    def peek(self):
        """
        Get the front element.
        
        Returns:
        int: The front element of the queue.
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        
        Returns:
        bool: True if the queue is empty, False otherwise.
        """
        return not self.stack1 and not self.stack2


if __name__ == "__main__":
    myQueue = MyQueue()
    myQueue.push(1)  # queue is: [1]
    myQueue.push(2)  # queue is: [1, 2] (leftmost is front of the queue)
    print(myQueue.peek())  # return 1
    print(myQueue.pop())  # return 1, queue is [2]
    print(myQueue.empty())  # return False
    print(myQueue.pop())  # return 2, queue is [empty]
    print(myQueue.empty())  # return True
   