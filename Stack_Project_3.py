class Stack:

    def __init__(self):
        # Write code here
        self.stack = ''

    def __iter__(self):
        return iter(self.stack)

    def __str__(self):
        return self.stack

    def push(self, b):
        if isinstance(b, list) or isinstance(b, str):
            for item in b:
                self.stack += item
        else:
            self.stack += b

    def top(self):
        return self.stack[-1]

    def pop(self):
        a = self.stack[-1]
        self.stack = self.stack[:-1]
        return a

    def size(self):
        return len(self.stack)

    def empty(self):
        if not self.stack:
            return 'true'

    def reset(self):
        self.stack = ''


def isBalanacedParentheses(s):
    # Write code here
    opening = ('(', '[', '{')
    closing = (')', ']', '}')
    count = {}
    my_stack = Stack()
    my_stack.push(s)

    for item in my_stack:
        if item in opening:
            my_stack.push(item)
            count[item] = count.get(item, 0) + 1
        elif item in closing:
            if not my_stack.empty() and my_stack.top() in opening:
                if (my_stack.top() == '(' and item == ')') or \
                   (my_stack.top() == '[' and item == ']') or \
                   (my_stack.top() == '{' and item == '}'):
                    my_stack.pop()
                    count[my_stack.top()] -= 1
                else:
                    return 'false'
            else:
                return 'false'

    # Check if all opening parentheses are matched
    for key in count:
        if count[key] != 0:
            return 'false'

    return 'true' if my_stack.empty() else 'false'


