import stack

def are_brackets_balanced(expr):
    s = stack.Stack()
    for char in expr:
        if char in ['(', '{', '[']:
            s.push(char)
        if char in [')', '}', ']']:
            if s.size == 0:
                return False
            current_char = s.pop()
            if current_char == '(':
                if char != ')':
                    return False
            if current_char == '{':
                if char != '}':
                    return False
            if current_char == '[':
                if char != ']':
                    return False

    if s.size == 0:
        return Truepyth
    return False
