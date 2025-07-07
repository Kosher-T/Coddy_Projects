class Stack:

    def __init__(self):
        # Write code here
        self.stack = []
        
    def push(self, a):
        self.stack.append(a)

    def top(self):
        return self.stack[-1]

    def pop(self):
        return self.stack.pop(-1)

    def size(self):
        return len(self.stack)

    def empty(self):
        if not self.stack:
            return 'true'
        return 'false'


def reverse(a):
    # Write code here
    new = []
    obj = Stack()
    for each in a:
        obj.push(each)
    for each in range(0, len(a)):
        new.append(obj.pop())
    return new