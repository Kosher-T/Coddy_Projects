class Stack:

    def __init__(self):
        # Write code here
        self.elem = []
        
    def push(self, a):
        self.elem.append(a)

    def top(self):
        return self.elem[-1]

    def pop(self):
        return self.elem.pop(-1)

    def size(self):
        return len(self.elem)