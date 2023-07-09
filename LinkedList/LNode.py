class LNode():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


    # def __repr__(self):
    #     return repr(self.data)

    def __repr__(self):
        return "(" + repr(self.data) + ", " + repr(id(self.next)) + ")"



# a = LNode(1)
# b = LNode(2)
# c = LNode(3)
#
# a.next = b
# b.next = c
#
# print(f"a = {a}")
# print(f"b = {a.next}")
# print(f"c = {a.next.next}")
