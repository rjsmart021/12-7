class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Create the binary tree as per the given structure
root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.left.left = TreeNode(40)
root.left.right = TreeNode(20)
root.right.left = TreeNode(60)
root.right.right = TreeNode(80)

def inorder_traversal(root):  # In-order Traversal of the binary tree
    if root:
        inorder_traversal(root.left)
        print(root.val, end=' ')
        inorder_traversal(root.right)

def preorder_traversal(root): # Pre-order Traversal of the binary tree
    if root:
        print(root.val, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root): # Post-order Traversal of the binary tree
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val, end=' ')



# Testing traversal functions
print("In-order Traversal:")  # In-order Traversal
inorder_traversal(root)
print("\nPre-order Traversal:")     # Pre-order Traversal
preorder_traversal(root)
print("\nPost-order Traversal:")  # Post-order Traversal
postorder_traversal(root)
