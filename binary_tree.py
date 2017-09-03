class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self, val):
        self.root = Node(val)

    def insert(self, val):
        self._insert(self.root, val)

    def _insert(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self._insert(node.left, val)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self._insert(node.right, val)

    def inorder_print(self):
        self._inorder_print(self.root)

    def _inorder_print(self, node):
        if node is None:
            return
        self._inorder_print(node.left)
        print(node.val)
        self._inorder_print(node.right)


bst = BST(9)
bst.insert(5)
bst.insert(11)
bst.insert(12)
bst.insert(2)
bst.insert(3)
bst.insert(7)
bst.insert(16)
bst.inorder_print()
