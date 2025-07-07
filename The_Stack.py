class Stack:

    def __init__(self):
        # Initialize an empty list to serve as the stack.
        self.items = []
        self.mini = []
        self.maxi = []

    def __str__(self):
        # Represent the stack as a string for easy printing.
        return str(self.items)

    def push(self, item):
        # Add an item to the top of the stack.
        self.items.append(item)

    def pop(self):
        # Remove and return the top item from the stack.
        # Check if the stack is empty before popping.
        if not self.is_empty():
            return self.items.pop()
        return None # Or raise an exception

    def top(self):
        # Return the top item without removing it.
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        # Return the number of items in the stack.
        return len(self.items)

    def is_empty(self):
        # Return True if the stack is empty, 'false' otherwise.
        # This should return a boolean, not a string.
        return len(self.items) == 0

    def min(self):
        return min(self.items)

    def max(self):
        return max(self.items)