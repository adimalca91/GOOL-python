from TNode import TNode

class BinarySearchTree():

    # A constructor that ONLY creates the tree
    # def __init__(self):
    #     self.root = None

    # A constructor that creates and initializes the elements in the tree
    def __init__(self, seq=None):
        self.root = None
        if seq != None:
            for key, data in seq:
                self.insert(key,data) # Using our insert method we wrote below.

    def lookup(self, key):
        return self.__lookup_node(self.root, key)

    def __lookup_node(self, node, key):
        if node == None:
            return None

        if key == node.key:
            return node
        elif key < node.key:
            return self.__lookup_node(node.left, key)
        return self.__lookup_node(node.right, key)

    def insert(self, key, data):
        if self.root == None:
            self.root = TNode(key, data)
        self.__insert_recursive(self.root, key, data)

    def __insert_recursive(self, node, key, data):
        if key == node.key:
            node.data = data

        elif key < node.key:
            if node.left == None:
                node.left = TNode(key, data)
            self.__insert_recursive(node.left, key, data)

        else:
            if node.right == None:
                node.right = TNode(key, data)
            self.__insert_recursive(node.right, key, data)

        return


    def find_minimum(self):
        current = self.root

        while(current.left != None):
            current = current.left

        return current

    def find_depth(self):
        return self.__depth_recursive(self.root)

    def __depth_recursive(self, node):
        if node == None:
            return -1
        return 1 + max(self.__depth_recursive(node.left), self.__depth_recursive(node.right))

    def __len__(self):
        return self.__len_recursive(self.root)

    def __len_recursive(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.__len_recursive(node.right) + self.__len_recursive(node.left)

    def inorder(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node == None:
            return
        self._inorder_recursive(node.left)     # L
        print(node.key, end=' ')               # D
        self._inorder_recursive(node.right)    # R


    def postorder(self):
        self._postorder_recursive(self.root)

    def _postorder_recursive(self, node):
        if node == None:
            return
        self._postorder_recursive(node.left)    # L
        self._postorder_recursive(node.right)   # R
        print(node.key, end=' ')                # D

    def preorder(self):
        self._preorder_recursive(self.root)

    def _preorder_recursive(self, node):
        if node == None:
            return
        print(node.key, end=' ')               # D
        self._preorder_recursive(node.left)    # L
        self._preorder_recursive(node.right)   # R




    def print_by_level(self):
        depth = self.find_depth()
        for level in range(depth+1):
            print(f"level {level}: ", end=' ')
            self._print_level(self.root, level)
            print()

    def _print_level(self, node, level):
        if node == None:
            return
        if level == 0:
            print(node.key, end=' ')
        else:
            self._print_level(node.left, level - 1)
            self._print_level(node.right, level - 1)






