class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        """
        Initialize a tree node.

        :param value: The value of the node.
        :param left: The left child of the node (default is None).
        :param right: The right child of the node (default is None).
        """
        self.value = value
        self.left = left
        self.right = right



def find_max_value(root):
    """
    Find the maximum value in a binary tree using in-order traversal.

    :param root: The root node of the binary tree.
    :return: The maximum value in the binary tree or a message if the tree is empty.
    """
    
    def inorder_traversal(node, max_val):
        """
        Perform in-order traversal on the tree and find the maximum value.

        :param node: The current node in the traversal.
        :param max_val: The current maximum value found.
        :return: The maximum value found in the subtree rooted at the given node.
        """
        if node:
            # Traverse the left subtree and update the max value
            max_val = inorder_traversal(node.left, max_val)
            
            # Update the max value if the current node's value is greater
            if node.value > max_val:
                max_val = node.value
            
            # Traverse the right subtree and update the max value
            max_val = inorder_traversal(node.right, max_val)
        
        return max_val


    if not root:
        return "The tree is empty"
    return inorder_traversal(root, root.value)

if __name__ == "__main__":
    
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(20)

    print(find_max_value(root)) 
