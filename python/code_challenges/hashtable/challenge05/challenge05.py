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
        Generate a hash for the given key using python standard hash function.
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

def convert_to_int_if_possible(value):
    """
    Converts the value to an integer if possible, otherwise returns the original value.
    """
    try:
        return int(value)
    except ValueError:
        return value

def find_intersection(arr1, arr2):
    """
    Finds the intersection of two arrays, converting strings to integers when possible.

    Parameters:
    arr1 (list): The first array, containing strings or integers.
    arr2 (list): The second array, containing strings or integers.

    Returns:
    list: A list of unique elements found in both arrays.
    """
    size = max(len(arr1), len(arr2))
    # Initialize a HashTable
    hash_table = HashTable(size)
    
    # Convert elements of arr1 to integers if possible and add them to the hash table
    for elem in arr1:
        elem = convert_to_int_if_possible(elem)
        if hash_table.get(elem) is None:
            hash_table.set(elem, 1)
        else:
            hash_table.set(elem, True)
    
    # Initialize a set for the intersection result to avoid duplicates
    intersection = set()
    
    # Convert elements of arr2 to integers if possible and check them against the hash table
    for elem in arr2:
        elem = convert_to_int_if_possible(elem)
        if hash_table.get(elem) is not None:
            intersection.add(elem)
    
    # Convert the set to a list and return
    return list(intersection)


if __name__ == "__main__":

    arr1 = ["1", "2", "2", "1"]
    arr2 = [2, 2]
    print(find_intersection(arr1, arr2))

    arr1 = [1, 2, 2, 1]
    arr2 = [2, 1]
    print(find_intersection(arr1, arr2))

    arr1 = ["1", "2", "2", "1"]
    arr2 = ["2", "1"]
    print(find_intersection(arr1, arr2))

