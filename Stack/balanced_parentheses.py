from stack import Stack

def check_balanced_parentheses(expression):
    stack = Stack()
    for char in expression:
        if char in ["(", "[", "{"]:
            stack.push(char)
        if char in [")", "]", "}"]:
            if stack.size == 0:
                return False
            current_char = stack.pop()
            if current_char == "(":
                if char != ")":
                    return False
            if current_char == "[":
                if char != "]":
                    return False
            if current_char == "{":
                if char != "}":
                    return False

    if stack.size == 0:
        return True
    return False



