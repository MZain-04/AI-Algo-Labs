class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v):
        if u not in self.adj:
            self.adj[u] = []
        self.adj[u].append(v)
        # Ensure destination node exists in the dictionary
        if v not in self.adj:
            self.adj[v] = []

#Iterative
    
    def dfs_stack(self, start, goal=None):
        stack = [start]
        visited = set()
        traversal = []

        print(f" DFS Traversal (Stack) starting from node '{start}' ")

        while stack:
            # S.top() and S.pop()
            v = stack.pop()

            if v not in visited:
                visited.add(v)
                traversal.append(v)
                print(f"Visited: {v}")

                # Stop if goal node is found
                if goal and v == goal:
                    print(f"Goal node '{goal}' reached!")
                    break

                # Push neighbors to stack (reversed to visit left-to-right)
                for neighbor in reversed(self.adj.get(v, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return traversal

# Recursive DFS
 
    def _dfs_util(self, v, visited):
        visited.add(v)
        print(v, end=" ")

        for neighbor in self.adj.get(v, []):
            if neighbor not in visited:
                self._dfs_util(neighbor, visited)

    def dfs_recursive(self, start):
        print(f"Recursive DFS starting from '{start}'")
        visited = set()
        self._dfs_util(start, visited)
        print()


g = Graph()

# add edges
g.add_edge('A', 'B')
g.add_edge('A', 'F')
g.add_edge('A', 'D')
g.add_edge('A', 'E')

g.add_edge('B', 'K')
g.add_edge('B', 'J')

g.add_edge('K', 'N')
g.add_edge('K', 'M')

g.add_edge('D', 'G')

g.add_edge('E', 'C')
g.add_edge('E', 'H')
g.add_edge('E', 'I')

g.add_edge('I', 'L')


traversal_path = g.dfs_stack(start='A', goal='Z')
print("\nFinal Traversal Sequence until Goal:", " -> ".join(traversal_path))