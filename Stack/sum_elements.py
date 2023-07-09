from stack import Stack

def sum_elements(stack):
    tmp_stack = Stack()
    sum = 0

    # The summing process
    while stack.is_empty() == False:
        temp = stack.pop()
        sum += temp
        tmp_stack.push(temp)

    # The returning process
    while tmp_stack.is_empty() == False:
        stack.push(tmp_stack.pop())

    return sum

s = Stack()

s.push(10)
s.push(10)
s.push(0)

print(sum_elements(s))