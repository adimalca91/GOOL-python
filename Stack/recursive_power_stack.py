from stack import Stack

def recursive_power_stack(stack):

    # Base Case
    if (stack.is_empty()):
        return

    head = stack.pop()**2
    recursive_power_stack(stack)
    stack.push(head)
    

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s)
recursive_power_stack(s)
print(s)
