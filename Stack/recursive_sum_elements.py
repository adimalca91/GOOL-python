from stack import Stack

def recursive_sum_elements(stack):
    # Base Case
    if(stack.is_empty()):
        return 0

    head = stack.pop()
    sum = recursive_sum_elements(stack) + head

    stack.push(head)

    return sum

s = Stack()

s.push(1)
s.push(2)
s.push(4)

print(recursive_sum_elements(s))