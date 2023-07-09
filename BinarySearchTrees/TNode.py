class TNode:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.right = None
        self.left = None

    def __repr__(self):
        return f"{self.key} : {self.data}"

    
