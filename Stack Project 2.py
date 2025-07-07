class Stack:

    def __init__(self):
        # Write code here
        self.stack = []

    def push(self, b):
        if isinstance(b, list):
            for item in b:
                self.stack.append(item)
        else:
            self.stack.append(b)

    def top(self):
        return self.stack[-1]

    def pop(self):
        return self.stack.pop(-1)

    def size(self):
        return len(self.stack)

    def empty(self):
        if not self.stack:
            return 'true'

    def reset(self):
        self.stack = []

    def __iter__(self):
        return iter(self.stack)

    def __str__(self):
        return f"Stack({self.stack})"


def nse(a):
    # Initialize variables I will need. I will skip the first element of a
    # a = [3, 4, 2, 7, 5, 8]
    result = [-1]
    b = a[1:]
    # create object of the stack first
    my_stack = Stack()
    my_stack.push(a[0])  # Push the first element of a to the stack
    for index, value in enumerate(b):
        if index == 0:
            my_stack.push(value)
        else:
            my_stack.push(b[0:index+1])
        for item in my_stack.stack:
            if item < value:
                result.append(item)
                break
            else:
                result.append(-1)
        my_stack.reset()

    return result

# Example usage
if __name__ == "__main__":
    print(nse([3, 4, 2, 7, 5, 8]))  # Output: [-1, -1, 3, -1, 2, 2]  # Output: Stack([])