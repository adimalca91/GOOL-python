from LNode import LNode

class LinkedList():
    def __init__(self):
        self.head = None

    def pre_append(self, data):
        node = LNode(data)
        node.next = self.head
        self.head = node

    def __repr__(self):
        if self.head == None:
            return "[]"
        s = "["
        curr_node = self.head
        while curr_node:
            s += repr(curr_node) + ", "
            curr_node = curr_node.next
        return s[:-2] + "]"   # slicing here depends on the way the text is shown in the list - spaces and commas.


    def __len__(self):
        length = 0
        iterative_node = self.head
        while iterative_node:
            length += 1
            iterative_node = iterative_node.next
        return length


    def sum(self):
        sum = 0
        iterative_node = self.head
        while iterative_node:
            sum += iterative_node.data
            iterative_node = iterative_node.next
        return sum


    def find(self, data):
        iterative_node = self.head
        while iterative_node:
            if data == iterative_node.data:
                return iterative_node
            iterative_node = iterative_node.next
        return None

    # def __getitem__(self, index):           # ADI implementation
    #     if index in range(self.__len__()):
    #         iterative_node = self.head
    #         for i in range(index):
    #             iterative_node = iterative_node.next
    #         return iterative_node.data
    #     raise IndexError("Index out of range error")


    def __getitem__(self, index):
        assert 0 <= index < len(self)
        iterative_node = self.head
        for i in range(0, index):
            iterative_node = iterative_node.next
        return iterative_node.data


    def __setitem__(self, index, value):
        assert 0 <= index < len(self)
        iterative_node = self.head
        for i in range(0, index):
            iterative_node = iterative_node.next
        iterative_node.data = value

    # def insert(self, value, index):      # ADI implementation
    #     assert 0 <= index <= len(self)
    #     new_node = LNode(value, self.head)
    #     iterative_node = self.head
    #     if index == 0:
    #         self.pre_append(value)
    #         return
    #     else:
    #         for i in range(index-1):
    #             iterative_node = iterative_node.next
    #         new_node.next = iterative_node.next
    #         iterative_node.next = new_node


    def insert(self, value, index):
        assert 0 <= index <= len(self)
        if index == 0:
            self.pre_append(value)
            return
        iterative_node = self.head
        for i in range(0, index-1):
            iterative_node = iterative_node.next
        tmp = iterative_node.next
        iterative_node.next = LNode(value)
        iterative_node.next.next = tmp


    def delete(self, index):
        assert 0 <= index < len(self)
        if index == 0:
            self.head = self.head.next
            return
        iterative_node = self.head
        for i in range(0, index-1):
            iterative_node = iterative_node.next
        iterative_node.next = iterative_node.next.next

