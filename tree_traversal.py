class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def in_order_trav(self):
        self._in_order_trav(self.root)
        print()

    def _in_order_trav(self, node):
        if node:
            self._in_order_trav(node.left)
            print(node.key, end=" ")
            self._in_order_trav(node.right)

    def pre_order_trav(self):
        self._pre_order_trav_recur(self.root)
        print()

    def _pre_order_trav_recur(self, node):
        if node:
            print(node.key, end=" ")
            self._pre_order_trav_recur(node.left)
            self._pre_order_trav_recur(node.right)

    def post_order_trav(self):
        self._post_order_trav_recur(self.root)
        print()

    def _post_order_trav_recur(self, node):
        if node:
            self._post_order_trav_recur(node.left)
            self._post_order_trav_recur(node.right)
            print(node.key, end=" ")

    def print_tree(self):
        self._print_tree_recur(self.root, 0)

    def _print_tree_recur(self, node, depth):
        if node is None:
            return
        self._print_tree_recur(node.right, depth + 1)
        print("   " * depth + str((node.key)))
        self._print_tree_recur(node.left, depth + 1)



if __name__ == "__main__":
    tree = BinaryTree()

    # Insert keys
    keys = [50, 30, 70, 40, 20, 60, 80]
    for key in keys:
        tree.insert(key)

    # In-order traversal
    print('In-order traversal:')
    tree.in_order_trav()

    # Pre-order traversal
    print('Pre-order traversal:')
    tree.pre_order_trav()

    # Post-order traversal
    print('Post-order traversal:')
    tree.post_order_trav()

    # Print Tree Structure
    print('Binary tree structure:')
    tree.print_tree()
