class Queue:
    def __init__(self, max_size, size=0, front=0, tail=0):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.size = size
        self.front = front
        self.tail = tail

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def __repr__(self):
        s = ""
        for i in range(self.size):
            index = int((self.front + i) % self.max_size)
            s += f"{self.queue[index]}, "
        return s[:-2]

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full")
        else:
            self.queue[self.tail] = data
            self.tail = int((self.tail + 1) % self.max_size)
            self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print(f"{self.queue[self.front]} is removed")
            self.front = int((self.front + 1) % self.max_size)
            self.size -= 1


q = Queue(5)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

print(q)

q.dequeue()
q.dequeue()
q.dequeue()

print(q)

q.enqueue(10)
print(q)

q.enqueue(11)
q.enqueue(12)
print(q)

q.enqueue(12)
q.enqueue(12)


