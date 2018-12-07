class Stack:
    def __init__(self, iterable=None):
        self.stack = []
        if iterable:
            for item in iterable:
                self.stack.append(item)

    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            raise IndexError("pop from empty stack")
    
    def top(self):
        try:
            return self.stack[-1]
        except IndexError:
            raise IndexError("nothing in the empty stack")

    def is_empty(self):
        return len(self.stack) == 0