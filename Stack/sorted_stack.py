from stack import Stack


# ADI'S IMPLEMENTATION

def sort_stack(stack):
    sorted_stack = Stack()
    while(stack.size != 0):
        temp = stack.pop()
        while(sorted_stack.size != 0 and sorted_stack.top() > temp):
            stack.push(sorted_stack.pop())
        sorted_stack.push(temp)
    return sorted_stack


def sortStack(stack):
    tmp_stack = Stack()
    while(stack.is_empty() == False):
        temp = stack.pop()

        while (tmp_stack.is_empty() == False and tmp_stack.top() > temp):
            stack.push(tmp_stack.pop())

        tmp_stack.push(temp)

    return tmp_stack


s = Stack()

s.push(20)
s.push(2)
s.push(30)
s.push(4)
s.push(35)
s.push(4)
s.push(33)
print("Before Sorting: \n")
print(s)
print(" \nAfter sorting \n")
print(sortStack(s))


