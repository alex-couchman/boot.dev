from stack import Stack


def is_balanced(input_str):
    stack = Stack()
    for char in input_str:
        if char == "(":
            stack.push(char)
        if char == ")":
            if stack.pop() == None:
                return False
    if stack.size() != 0:
        return False
    return True
