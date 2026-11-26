
# Minimax Algorithm

def minimax(node, maximizingPlayer):

    # Base case: If node is a leaf
    if isinstance(node, int):
        return node

    if maximizingPlayer:

        bestValue = float('-inf')

        # Visit every child
        for child in node:
            value = minimax(child, False)

            bestValue = max(bestValue, value)

        return bestValue

    else:

        bestValue = float('inf')

        # Visit every child
        for child in node:
            value = minimax(child, True)

            bestValue = min(bestValue, value)

        return bestValue


# Game tree
tree = [
    [[3, 5], [6, 9]],
    [[1, 2], [0, -1]]
]

# Call minimax
result = minimax(tree, True)

print("Optimal value:", result)
