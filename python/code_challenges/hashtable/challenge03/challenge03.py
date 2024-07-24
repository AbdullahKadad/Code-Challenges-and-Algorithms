class Node:
    def __init__(self, data):
        """
        Initializes a Node with the given data and sets the next node to None.
        """
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        """
        Initializes an empty LinkedList with the head set to None.
        """
        self.head = None

    def add(self, data):
        """
        Adds a node with the given data to the end of the LinkedList.
        """
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def find(self, key):
        """
        Finds and returns the node with the given key in the LinkedList. 
        Returns None if the key is not found.
        """
        current = self.head
        while current:
            if current.data[0] == key:
                return current
            current = current.next
        return None

    def __iter__(self):
        """
        Allows iteration over the LinkedList, yielding the data of each node.
        """
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __str__(self):
        """
        Returns a string representation of the LinkedList.
        """
        return str(list(self))

class HashTable:
    def __init__(self, size=10):
        """
        Initializes a HashTable with the given size. Default size is 10.
        """
        self.size = size
        self.map = [None] * size

    def hash_key(self, key):
        """
        Generates a hash for the given key using the Python standard hash function.
        """
        return hash(key) % self.size

    def set(self, key, value):
        """
        Sets the key-value pair in the HashTable. Handles collisions using chaining.
        """
        hashed_key = self.hash_key(key)
        if self.map[hashed_key] is None:
            self.map[hashed_key] = [key, value]
        else:
            if isinstance(self.map[hashed_key], LinkedList):
                existing_node = self.map[hashed_key].find(key)
                if existing_node:
                    existing_node.data[1] = value
                else:
                    self.map[hashed_key].add([key, value])
            else:
                existing_pair = self.map[hashed_key]
                if existing_pair[0] == key:
                    existing_pair[1] = value
                else:
                    chain = LinkedList()
                    chain.add(existing_pair)
                    chain.add([key, value])
                    self.map[hashed_key] = chain

    def get(self, key):
        """
        Retrieves the value for the given key from the HashTable.
        """
        hashed_key = self.hash_key(key)
        bucket = self.map[hashed_key]
        if bucket is None:
            return None
        elif isinstance(bucket, list):
            if bucket[0] == key:
                return bucket[1]
            return None
        else:
            for pair in bucket:
                if pair[0] == key:
                    return pair[1]
            return None

def sum_of_unique_elements(nums):
    """
    Finds the summation of unique elements in the array and returns the summation.
    Unique elements of an array are the elements that appear exactly once in the array.

    Args:
        nums (list): List of integers.

    Returns:
        int: Sum of unique elements.
    """
    hash_table = HashTable()

    # Count the occurrences of each element in the array
    for num in nums:
        count = hash_table.get(num)
        if count is None:
            hash_table.set(num, 1)
        else:
            hash_table.set(num, count + 1)

    # Find the unique elements and sum them
    unique_sum = 0
    for num in nums:
        count = hash_table.get(num)
        if count == 1:
            unique_sum += num

    return unique_sum


if __name__ == "__main__":
    nums_1 = [] # 0
    nums_2 = [1, 2, 3, 4, 5] # 15
    nums_3 = [1, 1, 2, 2, 3, 3] # 0
    nums_4 = [1, 2, 2, 3, 4, 4, 5] # 9
    nums_5 = [42] # 42
    nums_6 = [7, 7, 7, 7, 7] # 0 
    nums_7 = [1, 2, 3, 1, 2, 3, 4] # 4
    nums_8 = [-1, -2, -3, -1, -2, -4] # -7
    nums_9 = [-1, 1, -2, 2, -3, 3, -1, 1, -2, 2] # 0
    nums_10 = [0, 1, 2, 0, 3, 2] # 4

    result_1 = sum_of_unique_elements(nums_1)
    print(result_1)
    result_2 = sum_of_unique_elements(nums_2)
    print(result_2)
    result_3 = sum_of_unique_elements(nums_3)
    print(result_3)
    result_4 = sum_of_unique_elements(nums_4)
    print(result_4)
    result_5 = sum_of_unique_elements(nums_5)
    print(result_5)
    result_6 = sum_of_unique_elements(nums_6)
    print(result_6)
    result_7 = sum_of_unique_elements(nums_7)
    print(result_7)
    result_8 = sum_of_unique_elements(nums_8)
    print(result_8)
    result_9 = sum_of_unique_elements(nums_9)
    print(result_9)
    result_10 = sum_of_unique_elements(nums_10)
    print(result_10)