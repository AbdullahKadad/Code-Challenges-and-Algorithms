class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        TreeNode constructor.

        Args:
        - val (int): The value of the node.
        - left (TreeNode, optional): The left child node.
        - right (TreeNode, optional): The right child node.
        """
        self.val = val
        self.left = left
        self.right = right

def arrayToBST(array):
    """
    Constructs a balanced Binary Search Tree (BST) from an array.

    Args:
    - array (list of int): An array of integers.

    Returns:
    - TreeNode: The root node of the constructed BST.
    """
    
    if not array:
        return None

    # Sort the array
    sortedArray = sorted(array)
    
    def sortedArrayToBST(sortedArray):
        if not sortedArray:
            return None

        mid = len(sortedArray) // 2
        root = TreeNode(sortedArray[mid])

        root.left = sortedArrayToBST(sortedArray[:mid])
        root.right = sortedArrayToBST(sortedArray[mid + 1:])

        return root

    return sortedArrayToBST(sortedArray)

def inOrderTraversal(root, values):
    """
    Performs in-order traversal of a binary tree and stores node values in a list.

    Args:
    - root (TreeNode): The root node of the tree.
    - values (list): An empty list to store node values in-order.
    """
    if root:
        inOrderTraversal(root.left, values)
        values.append(root.val)
        inOrderTraversal(root.right, values)

def inOrderTraversalWithNodeValues(root, values):
    """
    Performs in-order traversal of a binary tree and stores node values in a list, including None for null nodes.

    Args:
    - root (TreeNode): The root node of the tree.
    - values (list): A list to store node values in-order, including None for null nodes.
    """
    if root is None:
        values.append(None)
        return
    
    inOrderTraversalWithNodeValues(root.left, values)
    values.append(root.val)
    inOrderTraversalWithNodeValues(root.right, values)

if __name__ == "__main__":
    sortedArray = [5, 2, 4, 0, 1, 3]
    tree = arrayToBST(sortedArray)
    values_in_order = []
    values_in_order_none = []
    inOrderTraversal(tree, values_in_order)
    inOrderTraversalWithNodeValues(tree, values_in_order_none)
    print("Without None", values_in_order)
    print("With None", values_in_order_none)