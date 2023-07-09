from stack import Stack

def is_sorted_stack(stack):
    tmp_stack = Stack()
    tmp_stack.push(stack.pop())
    is_sorted = True

    while(stack.is_empty() == False):
        temp = stack.pop()
        if (tmp_stack.top() >= temp):
            tmp_stack.push(temp)
        else:
            is_sorted = False
            break

    while(tmp_stack.is_empty() == False):
        stack.push(tmp_stack.pop())

    return is_sorted


def is_sorted(stack):
    tmp_stack = Stack()

    while(stack.is_empty() == False):
        tmp_stack.push(stack.pop())

        if stack.is_empty():
            # Returning Process
            while(tmp_stack.is_empty() == False):
                stack.push(tmp_stack.pop())
            return True

        if tmp_stack.top() < stack.top():
            # Returning Process
            while(tmp_stack.is_empty() == False):
                stack.push(tmp_stack.pop())
            return False


s = Stack()

s.push(1)
s.push(2)
s.push(3)
s.push(3)
s.push(3)
s.push(6)
s.push(17)

print(is_sorted_stack(s))
