class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    # Breadth First Search - BFS is level-order, visiting a node's children before vising it's grand-children
    # Depth First Search - DFS has 3 ways, inorder, preorder and postorder, it go deep to visit all decendants of one child,
    # then visit all decendants of another child.
    def __init__(self, root):
        # convert the input to a Node object then save it as the root of the tree, so now the root has value, left and right
        self.root = Node(root)

    def inorder_print(self, root):
        if root:
            self.preorder_print(root.left)
            print(root.value)
            self.preorder_print(root.right)

    def preorder_print(self, root):
        if root:
            print(root.value)
            self.preorder_print(root.left)
            self.preorder_print(root.right)

    def postorder_print(self, root):
        if root:
            self.preorder_print(root.left)
            self.preorder_print(root.right)
            print(root.value)

    #       1
    #     /   \
    #    3     4
    #   / \   / \
    #  7   8 7   9

tree = BinaryTree(1)
tree.root.left = Node(3)
tree.root.right = Node(4)
tree.root.left.left = Node(7)
tree.root.left.right = Node(8)
tree.root.right.left = Node(7)
tree.root.right.right = Node(9)


tree.preorder_print(tree.root)
