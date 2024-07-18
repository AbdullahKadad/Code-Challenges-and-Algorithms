class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        """
        Initialize a tree node.

        Args:
            value (int): The value of the node.
            left (TreeNode, optional): The left child of the node. Defaults to None.
            right (TreeNode, optional): The right child of the node. Defaults to None.
        """
        self.value = value
        self.left = left
        self.right = right

def max_height(root):
    """
    Calculate the maximum height of a binary tree.

    The height of a binary tree is defined as the number of edges on the longest path
    from the root to a leaf.

    Args:
        root (TreeNode): The root node of the binary tree.

    Returns:
        int: The maximum height of the binary tree. Returns -1 if the tree is empty.
    """
    if root is None:
        return -1  
    left_height = max_height(root.left)
    right_height = max_height(root.right)
    return max(left_height, right_height) + 1

if __name__ == "__main__":
    # Example tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5

    # Creating the tree nodes
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Finding the maximum height
    print(max_height(root))
