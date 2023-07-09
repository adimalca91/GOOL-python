from LinkedList import *

# step 1 - creating the linkedlist object
linkedlist = LinkedList()


# step 2 - creating the LNodes
a = LNode(1)
b = LNode(2)
c = LNode(3)


# step 3 - creating the connections between the LNodes in the linkedlist
linkedlist.head = a
linkedlist.head.next = b
linkedlist.head.next.next = c


print(linkedlist.head)
print(linkedlist.head.next)
print(linkedlist.head.next.next)


# pre_append method

linkedlist.pre_append(4)

print("\nAfter adding a new node to the beggining of the linked list\n")

print(linkedlist.head)
print(linkedlist.head.next)
print(linkedlist.head.next.next)
print(linkedlist.head.next.next.next)


print("\nNew linkedlist using the pre_append method:\n")

linkedlist1 = LinkedList()
linkedlist1.pre_append(1)
linkedlist1.pre_append(5.5)
linkedlist1.pre_append("a")

print(linkedlist1.head)
print(linkedlist1.head.next)
print(linkedlist1.head.next.next)

print("\nAftert calling the __repr__ method on the linkedlist object - \n")
print(linkedlist1)

print(id(None))

print("\nAftert calling the __len__ method on the linkedlist object - \n")

print(len(linkedlist1))

print("\nAftert calling the __getitem__ method on the linkedlist object - \n")

print(linkedlist1[2])


print("\nAftert calling the insert() method on the linkedlist object - \n")


linkedlist1.insert(16,2)

print(linkedlist1)


linkedlist1.delete(2)

print(linkedlist1)
