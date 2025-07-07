class Stack:
    """
    A more conventional Stack implementation using a Python list.
    Using a list is more efficient than string concatenation.
    """
    def __init__(self):
        # Initialize an empty list to serve as the stack.
        self.items = []

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

def is_balanced_parentheses(s):
    """
    Checks if a string of parentheses is balanced using a stack.

    Args:
        s: The input string containing parentheses.

    Returns:
        True if the parentheses are balanced, 'false' otherwise.
    """
    # Create an instance of our stack.
    stack = Stack()
    
    # A mapping of closing brackets to their corresponding opening brackets.
    # This makes the checking logic cleaner.
    matching_bracket = {')': '(', ']': '[', '}': '{'}
    
    # A set of opening brackets for quick lookups.
    opening_brackets = set(['(', '[', '{'])

    # Iterate through each character in the input string.
    for char in s:
        # If the character is an opening bracket, push it onto the stack.
        if char in opening_brackets:
            stack.push(char)
        # If the character is a closing bracket...
        elif char in matching_bracket:
            # If the stack is empty, it means we have a closing bracket
            # without a matching opener, so it's unbalanced.
            if stack.is_empty():
                return 'false'
            
            # Pop the top element and check if it's the matching
            # opening bracket for the current closing bracket.
            # If it's not a match, the string is unbalanced.
            if stack.pop() != matching_bracket[char]:
                return 'false'

    # After the loop, if the stack is empty, it means every opening
    # bracket had a matching closing bracket. Otherwise, it's unbalanced.
    return stack.is_empty()