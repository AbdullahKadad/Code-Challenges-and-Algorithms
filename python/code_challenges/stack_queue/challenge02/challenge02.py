class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self.stack = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.stack.append(item)

    def pop(self):
        """Remove and return the item from the top of the stack."""
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def is_valid(self, s) :
        """
        Check if a given string of brackets is valid.
        
        Args:
            s (str): The input string containing brackets.
        
        Returns:
            bool: True if the string is valid, False otherwise.
        """
        self.stack = []  # Reset stack
        bracket_map = {')': '(', '}': '{', ']': '['}  # Map of closing to opening brackets
        for char in s:
            if char in bracket_map.values():  # If it's an opening bracket
                self.push(char)
            elif char in bracket_map.keys():  # If it's a closing bracket
                if self.is_empty() or bracket_map[char] != self.pop():
                    return False
            else:
                # Ignore non-bracket characters
                continue
        return self.is_empty()

if __name__ == "__main__":
    stack = Stack()
    print(stack.is_valid("()"))
    print(stack.is_valid("()[]{}"))
    print(stack.is_valid("[({}]"))
    print(stack.is_valid("[(hello)()]"))
    print(stack.is_valid("[{(())}]"))
    print(stack.is_valid("{{}}"))
    print(stack.is_valid("{{[[(())]]}}"))
    print(stack.is_valid("{[}"))
