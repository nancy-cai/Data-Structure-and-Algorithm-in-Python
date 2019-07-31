class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
        
class BinaryTree(object):
    def __init__(self, root):
        # convert the input to a Node object then save it as the root of the tree, so now the root has value, left and right
        self.root = Node(root) 


    #       1
    #     /   \
    #    3     4
    #   / \   / \
    #  7   8 7   9
        
tree = BinaryTree(1)
tree.root.left = 3
tree.root.right = 4
tree.root.left.left = 7
tree.root.left.right = 8
tree.root.right.left = 7
tree.root.right.right = 9