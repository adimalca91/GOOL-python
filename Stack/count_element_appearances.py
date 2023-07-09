from stack import Stack


# ADI'S IMPLEMENTATION

def count_appearances(stack, x):
    tmp_stack = Stack()
    count = 0

    # The 'counting process'
    while stack.is_empty() == False:
        temp = stack.pop()
        if temp == x:
            count += 1
        tmp_stack.push(temp)

    # The 'returning process'
    while tmp_stack.is_empty() == False:
        stack.push(tmp_stack.pop())

    return count


s = Stack()

s.push(30)
s.push(20)
s.push(2)
s.push(30)
s.push(4)
s.push(35)
s.push(4)
s.push(30)
s.push(33)

print(count_appearances(s, 20))