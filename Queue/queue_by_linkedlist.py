from Node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.tail = None

    def is_empty(self):
        return self.front == None

    def enqueue(self, data):
        new_element = Node(data)
        if self.front is None:
            self.front = self.tail = new_element
        else:
            self.tail.next = new_element
            self.tail = new_element


    def dequeue(self):
        if self.is_empty():
            return None
        data = self.front.data
        self.front = self.front.next
        # Check if the queue is empty
        if self.front is None:
            self.tail = None
        return data



    def __repr__(self):
        if self.is_empty():
            return "[]"

        s = "["
        temp_queue = Queue()

        # Adding the elements to the string s
        while self.is_empty() == False:
            s += f"{self.front.data}, "
            temp_queue.enqueue(self.dequeue()) # This is the way to basically "increment" the front to point at the next node.

        # Returning the nodes back to the original queue
        while temp_queue.is_empty() == False:
            self.enqueue(temp_queue.dequeue())

        return s[:-2] + "]"


    # ADI'S IMPLEMENTATION -
    def __len__(self):
        if self.is_empty():
            return 0

        temp = self.front
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
        return count

    # def __len__(self):
    #     if self.is_empty():
    #         return 0
    #
    #     counter = 0
    #     temp_queue = Queue()
    #     while self.is_empty() is False:
    #         counter += 1
    #         temp_queue.enqueue(self.dequeue()) # The way to "increment" the while loop
    #
    #     # Return all the elements back to original queue
    #     while temp_queue.is_empty() is False:
    #         self.enqueue(temp_queue.dequeue())
    #
    #     return counter


    # ADI'S IMPLEMENTATION -
    def count_data_appearances(self, data):
        if self.is_empty():
            return 0

        count = 0
        temp = self.front
        while temp != None:
            if temp.data == data:
                count += 1
            temp = temp.next

        return count


def merge_two_queues(q1, q2):
    q3 = Queue()

    while q1.is_empty() == False and q2.is_empty == False:
        q3.enqueue(q1.dequeue())
        q3.enqueue(q2.dequeue())

    while q1.is_empty() is False:
        q3.enqueue(q1.dequeue())

    while q2.is_empty() is False:
        q3.enqueue(q2.dequeue())

    return q3



q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(4)
q.enqueue(4)
print(q)
print(len(q))
print(q)

# q.dequeue()
# q.dequeue()
#
# print(q)
# print(len(q))
#
# q.dequeue()
# q.dequeue()
# q.dequeue()
#
# print(q)
# print(len(q))

print(q.count_data_appearances(4))


q1 = Queue()
q1.enqueue(1)
q1.enqueue(2)

q2 = Queue()
q2.enqueue(40)
q2.enqueue(50)
q2.enqueue(60)
q2.enqueue(70)
q2.enqueue(80)

print(merge_two_queues(q1, q2))