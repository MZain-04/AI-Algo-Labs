# Implementation of Queue in Python

class Queue:
    def __init__(self):
        self.items = []

    # Add an item to the queue
    def enqueue(self, item):
        self.items.append(item)
        print(item, "added to queue")

    # Remove an item from the queue
    def dequeue(self):
        if len(self.items) == 0:
            print("Queue is empty")
        else:
            item = self.items.pop(0)
            print(item, "removed from queue")

    # Display the queue
    def display(self):
        print("Queue:", self.items)


# Create Queue
q = Queue()

# Add items
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

# Display queue
q.display()

# Remove item
q.dequeue()

# Display queue again
q.display()