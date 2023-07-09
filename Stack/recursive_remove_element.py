from stack import Stack

def recursive_remove_element(stack, x):
    # Base Case
    if(stack.is_empty()):
        return

    # Reduce the problem
    head = stack.pop()
    if(head == x):
        return
    recursive_remove_element(stack,x)
    stack.push(head)


def remove(stack,x):
    if stack.is_empty():
        return

    if stack.top() == x:
        stack.pop()
        return

    top = stack.pop()
    remove(stack, x)
    stack.push(top)



s = Stack()
s.push(1)
s.push(2)
s.push(4)
print(s)
recursive_remove_element(s,1)
print(s)