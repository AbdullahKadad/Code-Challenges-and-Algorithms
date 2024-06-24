class Node:
    def __init__(self, value):
        """
        Initializes a new node with the given value.
        
        Args:
            value (int): The value of the node.
        """
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        """
        Initializes an empty binary tree.
        """
        self.root = None

    def __str__(self):
        """
        Returns a string representation of the tree as an array.
        """
        if not self.root:
            return "[]"
        
        # Initialize a list to store nodes level by level
        nodes = [self.root]
        result = []
        
        while nodes:
            next_level_nodes = []
            current_level_values = []
            
            for node in nodes:
                if node:
                    current_level_values.append(node.value)
                    next_level_nodes.append(node.left)
                    next_level_nodes.append(node.right)
                else:
                    current_level_values.append(None)
                    
            result.extend(current_level_values)
            nodes = next_level_nodes
        
        # Remove trailing None values at the end of the result list
        while result and result[-1] is None:
            result.pop()
        
        return str(result)

def construct_tree(preorder, inorder):
    """
    Constructs and returns a Tree instance given preorder and inorder traversal arrays.
        
    Args:
    preorder (List[int]): The preorder traversal of the binary tree.
    inorder (List[int]): The inorder traversal of the binary tree.
        
    Returns:
    Tree: The constructed binary tree.
    """
    if not preorder or not inorder:
        return Tree()
    
    # The first element in preorder list is the root node
    root_value = preorder[0]
    root = Node(root_value)
    
    # Find the index of the root in inorder list
    root_index_in_inorder = inorder.index(root_value)
    
    # Elements left to the root_index_in_inorder in inorder list
    # are part of the left subtree
    left_inorder = inorder[:root_index_in_inorder]
    
    # Elements right to the root_index_in_inorder in inorder list
    # are part of the right subtree
    right_inorder = inorder[root_index_in_inorder + 1:]
    
    # The corresponding preorder segments
    left_preorder = preorder[1:1 + len(left_inorder)]
    right_preorder = preorder[1 + len(left_inorder):]
    
    # Recursively build the left and right subtrees
    root.left = construct_tree(left_preorder, left_inorder).root
    root.right = construct_tree(right_preorder, right_inorder).root
    
    tree = Tree()
    tree.root = root
    return tree

if __name__ == "__main__":
    # preorder = [-1] 
    # inorder = [-1]
    preorder = [3,9,20,15,7] 
    inorder = [9,3,15,20,7]
    # preorder = [1, 2, 4, 5, 3, 6, 7]
    # inorder = [4, 2, 5, 1, 6, 3, 7]
    
    # Construct the binary tree and assign the root
    tree = construct_tree(preorder, inorder)

    print(tree)