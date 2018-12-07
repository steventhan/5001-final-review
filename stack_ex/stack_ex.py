"""
1. Design Stack class such that:
    a. It can be initialized using an iterable (list, tuple, set)
    b. Has standard stack operations (push, pop, top, is_empty)
    c. Hides the fact that it's just a list
2. Write a function that take a stack and return its length. 
    Analyze running time.
"""

def find_stack_length(stack):
    length = 0
    temp = []
    while not stack.is_empty():
        temp.append(stack.pop())
        length += 1

    for element in temp[::-1]:
        stack.push(element)

    return length