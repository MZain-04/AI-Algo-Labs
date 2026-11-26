class Puzzle:
    def __init__(self):
        self.start = None
        self.goal = None

    # Add start and goal states
    def add_state(self, start, goal):
        self.start = start
        self.goal = goal

    # Count misplaced tiles
    def heuristic(self, state):
        count = 0

        for i in range(9):
            if state[i] != 0 and state[i] != self.goal[i]:
                count += 1

        return count

    # Generate possible next states

    def get_neighbours(self, state):
        neighbours = []
        empty = state.index(0)

        # Possible movements
        moves = []

        if empty >= 3:
            moves.append(-3)  # Up

        if empty <= 5:
            moves.append(3)   # Down

        if empty % 3 != 0:
            moves.append(-1)  # Left

        if empty % 3 != 2:
            moves.append(1)   # Right

        # Generate new states
        for move in moves:
            new_state = list(state)

            new_position = empty + move

            new_state[empty], new_state[new_position] = (new_state[new_position], new_state[empty])

            neighbours.append(tuple(new_state))

        return neighbours


    # A* Search
    def AStar(self):
        open_list = [self.start]
        close_list = []

        g_cost = {self.start: 0}
        paths = {self.start: [self.start]}

        while open_list:

            current = min(open_list,key=lambda s: g_cost[s] + self.heuristic(s))

            open_list.remove(current)

            print("\nCurrent State:")
            self.display(current)

            if current == self.goal:
                print("\nGoal Found!")
                print("Solution Path:")

                for state in paths[current]:
                    self.display(state)

                print("Total Moves:", g_cost[current])
                return

            close_list.append(current)

            for neighbour in self.get_neighbours(current):

                new_cost = g_cost[current] + 1

                if neighbour in close_list:
                    continue

                if neighbour not in g_cost or new_cost < g_cost[neighbour]:

                    g_cost[neighbour] = new_cost
                    paths[neighbour] = paths[current] + [neighbour]

                    if neighbour not in open_list:
                        open_list.append(neighbour)

        print("Goal not found!")

    # Display puzzle
    def display(self, state):
        for i in range(0, 9, 3):
            print(state[i:i+3])


# Create puzzle object
p = Puzzle()

# Add start and goal states
p.add_state(
    (1, 2, 3,
     5, 6, 0,
     7, 8, 4),

    (1, 2, 3,
     5, 8, 6,
     0, 7, 4)
)

# Run A* Search
p.AStar()