from Node import LNode

class LinkedList:
    def __init__(self):
        self.head = None


a = LNode(1)
b = LNode(2)
c = LNode(3)
linkedlist = LinkedList()
linkedlist.head = a
linkedlist.head.next = b
linkedlist.head.next.next = c
