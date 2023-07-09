class LNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


# a = LNode(1)
# b = LNode(2)
# c = LNode(3)
#
# a.next = b
# b.next = c
#
# print("a = ", a)
# print("b = ", a.next)
# print("c = ", a.next.next)
