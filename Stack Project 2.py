class Stack:

    def __init__(self):
        # Write code here
        self.stack = []

    def push(self, b):
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
    # create object of the stack first
    my_stack = Stack()
    # Need to push elements to the stack
    for current_index in range(len(a)):  # current_index = iter(1, 2, 3, 4, 5)
        for current_element in a[0:current_index]:  # current_element = iter(3, 4, 2, 7, 5, 8) (for current_index == 6, result = [-1, 3, -1, 2, 2]).
            my_stack.push(current_element)  # self.stack = []
        print(my_stack.stack)  # minimum = 
        
        '''
        if minimum == a[current_index]:  # a[current_index] = a[2] = 2. True
            result.append(-1)
        else:
            result.append(minimum)
    
    return result
'''

# Example usage
if __name__ == "__main__":
    print(nse([3, 4, 2, 7, 5, 8]))  # Output: [-1, -1, 3, -1, 2, 2]  # Output: Stack([])