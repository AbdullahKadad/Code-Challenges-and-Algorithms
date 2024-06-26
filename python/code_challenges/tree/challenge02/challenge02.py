class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

def are_trees_identical(p, q):
    """
    Check if two binary trees rooted at p and q are identical.

    Args:
    - p (Node): Root of the first binary tree.
    - q (Node): Root of the second binary tree.

    Returns:
    - bool: True if trees are identical, False otherwise.
    """
    if not p and not q:
        return True
    if not p or not q:
        return False
    
    # Initialize queues for BFS
    queue_p = [p]
    queue_q = [q]
    
    while queue_p and queue_q:
        node_p = queue_p.pop(0)
        node_q = queue_q.pop(0)
        
        # Check if nodes are not matching
        if not node_p and not node_q:
            continue
        if not node_p or not node_q:
            return False
        if node_p.val != node_q.val:
            return False
        
        # Add left children to the queues
        queue_p.append(node_p.left)
        queue_p.append(node_p.right)
        
        # Add right children to the queues
        queue_q.append(node_q.left)
        queue_q.append(node_q.right)
    
    # If all checks pass, trees are identical
    return True


# Helper function to create a binary tree from a list
def create_tree(nodes):
    if not nodes:
        return None
    root = Node(nodes[0])
    queue = [root]
    index = 1
    while queue:
        node = queue.pop(0)
        if index < len(nodes) and nodes[index] is not None:
            node.left = Node(nodes[index])
            queue.append(node.left)
        index += 1
        if index < len(nodes) and nodes[index] is not None:
            node.right = Node(nodes[index])
            queue.append(node.right)
        index += 1
    return root


if __name__ == "__main__":
   p = create_tree([1, 2, 3])
   q= create_tree([1, 2, 3])
   print(are_trees_identical(p, q))