
# Class to represent the graph using lists
class Graph:

    def __init__(self):
        # Each node has a list of its neighboring nodes
        self.nodes = ['A', 'B', 'F', 'D', 'E', 'K', 'J',
                      'G', 'C', 'H', 'I', 'N', 'M', 'L']

        self.neighbors = [
            ['B', 'F', 'D', 'E'],  # Neighbors of A
            ['K', 'J'],           # Neighbors of B
            [],                   # Neighbors of F
            ['G'],                # Neighbors of D
            ['C', 'H', 'I'],      # Neighbors of E
            ['N', 'M'],           # Neighbors of K
            [],                   # Neighbors of J
            [],                   # Neighbors of G
            [],                   # Neighbors of C
            [],                   # Neighbors of H
            ['L'],                # Neighbors of I
            [],                   # Neighbors of N
            [],                   # Neighbors of M
            []                    # Neighbors of L
        ]

    # Function to find the neighbors of a node
    def get_neighbors(self, node):
        index = self.nodes.index(node)
        return self.neighbors[index]


# Function to perform BFS and find the goal node
def bfs_search_goal(graph, start_node, goal_node):

    # List to keep track of visited nodes
    visited = [start_node]

    # A normal list works as a queue
    queue = [[start_node, [start_node]]]

    print(f"Starting BFS from '{start_node}' looking for '{goal_node}'...\n")

    while len(queue) > 0:

        # Remove the first item from the queue
        current_item = queue.pop(0)

        current_node = current_item[0]
        path = current_item[1]

        print(f"Checking node: {current_node}")

        # Check whether the current node is the goal
        if current_node == goal_node:
            print(f"\nSuccess! Found goal node '{goal_node}'.")
            print(f"Path to goal: {' -> '.join(path)}")
            return True

        # Visit each neighboring node
        for neighbor in graph.get_neighbors(current_node):

            if neighbor not in visited:

                # Mark the neighbor as visited
                visited.append(neighbor)

                # Save the path leading to this neighbor
                new_path = path + [neighbor]

                # Add the neighbor and its path to the queue
                queue.append([neighbor, new_path])

    # The goal was not found
    print(f"\nGoal node '{goal_node}' was not found in the graph.")
    return False


# Main program
if __name__ == "__main__":

    # Create a graph object
    tree_graph = Graph()

    # Search for G starting from A
    bfs_search_goal(tree_graph, 'A', 'G')

