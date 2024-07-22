import re

class HashTable:
    """
    A simple HashTable implementation using separate chaining for collision resolution.
    """

    def __init__(self, size=10):
        """
        Initializes a HashTable with the given size. Default size is 10.
        """
        self.size = size
        self.map = [None] * size

    def hash_key(self, key):
        """
        Generates a hash for the given key using Python's standard hash function.

        Args:
            key (str): The key to hash.

        Returns:
            int: The hashed value of the key.
        """
        return hash(key) % self.size

    def set(self, key, value):
        """
        Sets the key-value pair in the HashTable. Handles collisions using chaining.

        Args:
            key (str): The key to set.
            value (any): The value to associate with the key.
        """
        hashed_key = self.hash_key(key)

        if self.map[hashed_key] is None:
            self.map[hashed_key] = [key, value]
        else:
            if isinstance(self.map[hashed_key], LinkedList):
                self.map[hashed_key].add([key, value])
            else:
                existing_pair = self.map[hashed_key]
                chain = LinkedList()
                chain.add(existing_pair)
                chain.add([key, value])
                self.map[hashed_key] = chain

    def get(self, key):
        """
        Retrieves the value for the given key from the HashTable.

        Args:
            key (str): The key to retrieve.

        Returns:
            any: The value associated with the key, or None if the key is not found.
        """
        hashed_key = self.hash_key(key)
        if self.map[hashed_key] is None:
            return None
        elif isinstance(self.map[hashed_key], LinkedList):
            return self.map[hashed_key].find(key)
        else:
            return self.map[hashed_key][1] if self.map[hashed_key][0] == key else None

class Node:
    """
    A Node in a LinkedList, used for chaining in the HashTable.
    """

    def __init__(self, key, value):
        """
        Initializes a Node with a key-value pair.

        Args:
            key (str): The key of the node.
            value (any): The value of the node.
        """
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    """
    A simple LinkedList implementation for chaining in the HashTable.
    """

    def __init__(self):
        """Initializes an empty LinkedList."""
        self.head = None

    def add(self, pair):
        """
        Adds a new node with the given key-value pair to the end of the LinkedList.

        Args:
            pair (list): A list containing the key and value.
        """
        new_node = Node(pair[0], pair[1])
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find(self, key):
        """
        Finds the value associated with the given key in the LinkedList.

        Args:
            key (str): The key to find.

        Returns:
            any: The value associated with the key, or None if the key is not found.
        """
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

def find_first_repeated_word(s):
    """
    Finds the first repeated word in a given string.

    Args:
        s (str): The input string.

    Returns:
        str: The first repeated word, or "No Repetition" if no word is repeated.
    """
    words = re.findall(r'\b\w+\b', s)
    hash_table = HashTable()

    for word in words:
        word_lower = word.lower()
        if hash_table.get(word_lower) is not None:
            return hash_table.get(word_lower)
        hash_table.set(word_lower, word)
    
    return "No Repetition"

if __name__ == "__main__":
    input1 = "ASAC is a department at LTUC. ASAC teaches programming in LTUC."
    input2 = "I am learning programming at ASAC."

    print(find_first_repeated_word(input1))
    print(find_first_repeated_word(input2))
