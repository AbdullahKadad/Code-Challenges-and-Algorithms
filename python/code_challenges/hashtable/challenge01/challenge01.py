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

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        """
        Initializes a TreeNode with the given value and optional left and right children.
        """
        self.value = value
        self.left = left
        self.right = right

def find_pair_with_sum(root, target_sum):
    """
    Finds if there exists a pair of nodes in the binary search tree that sum to the target_sum.
    """
    hash_table = HashTable(size=10)

    def inorder_traverse(node):
        if node is None:
            return False
        
        if inorder_traverse(node.left):
            return True
        
        complement = target_sum - node.value
        if hash_table.get(complement) is not None:
            return True
        
        hash_table.set(node.value, True)

        return inorder_traverse(node.right)

    return inorder_traverse(root)

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(5)

    target_sum = 12
    print(find_pair_with_sum(root, target_sum))  # Output: True (5 + 7 = 12)
