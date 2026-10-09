# Lab 5 - Task 3
# Implementation of a Priority Queue in Python.


import heapq

class PriorityQueue:

  
    def __init__(self):
        # We'll store our items in a list and use heapq to keep it sorted
        self._queue = []
       
        self._index = 0
        
    def push(self, item, priority):
       
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1
        print(f"Inserted '{item}' with priority {priority}")
        
    def pop(self):
       
        if self.is_empty():
            print("The queue is empty! Nothing to pop.")
            return None
            
        # Pop the smallest item (based on priority)
        priority, index, item = heapq.heappop(self._queue)
        print(f"Popped '{item}' (priority was {priority})")
        return item
        
    def is_empty(self):
        
        return len(self._queue) == 0

if __name__ == "__main__":
    # Let's test our Priority Queue!
    print("--- Priority Queue Test ---\n")
    
    pq = PriorityQueue()
    
    
    pq.push("Do homework", priority=2)
    pq.push("Watch TV", priority=5)
    pq.push("Emergency: fix code bug!", priority=1)
    pq.push("Eat dinner", priority=3)
    
    print("\nProcessing tasks based on priority:")
    
    
    while not pq.is_empty():
        pq.pop()
