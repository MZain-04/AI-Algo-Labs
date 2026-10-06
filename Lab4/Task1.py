# Stack Implementation in Python

class Stack:

    def __init__(self):
        self.stack = []

    # Push element into stack
    def push(self,value):
        self.stack.append(value)
        print(value, "pushed into stack")

    # Remove top element
    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            value = self.stack.pop()
            print(value, "popped from stack")

    # Show top element
    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Top element:", self.stack[-1])

    # Check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Display stack
    def display(self):
        print("Stack:", self.stack)


# Create stack
s = Stack()

# Push elements
s.push(10)
s.push(20)
s.push(30)

# Display stack
s.display()

# Show top element
s.peek()

# Remove top element
s.pop()

# Display stack again
s.display()