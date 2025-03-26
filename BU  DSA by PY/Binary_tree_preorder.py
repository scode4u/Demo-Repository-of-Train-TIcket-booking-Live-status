class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(arr, index=0):
    """Recursively constructs the binary tree from the preorder list representation."""
    if index >= len(arr) or arr[index] == -1:
        return None, index + 1
    
    root = Node(arr[index])
    index += 1
    
    # Build left subtree
    root.left, index = build_tree(arr, index)
    
    # Build right subtree
    root.right, index = build_tree(arr, index)
    
    return root, index

def preorder_traversal(root):
    """Performs preorder traversal on the binary tree."""
    if root is None:
        return []
    
    # Visit the node, then left subtree, then right subtree
    return [root.value] + preorder_traversal(root.left) + preorder_traversal(root.right)

# Input array representing the tree in preorder format
arr = [1, 2, 4, -1, -1, 5, -1, -1, 3, -1, 6, -1, -1]

# Construct the binary tree
root, _ = build_tree(arr)

# Perform preorder traversal
preorder_result = preorder_traversal(root)

# Output the result of the preorder traversal
print("Preorder Traversal:", preorder_result)
