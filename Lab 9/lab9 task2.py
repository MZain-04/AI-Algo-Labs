
# Alpha-Beta Pruning Algorithm

def alpha_beta(node, alpha, beta, maximizingPlayer):

    # Base case: If node is a leaf
    if isinstance(node, int):
        return node

    if maximizingPlayer:

        bestValue = float('-inf')

        for child in node:

            value = alpha_beta(child, alpha, beta, False)

            bestValue = max(bestValue, value)

            # Update alpha
            alpha = max(alpha, bestValue)

            # Check pruning condition
            if beta <= alpha:
                print("Pruning remaining branch")
                break

        return bestValue

    else:

        bestValue = float('inf')

        for child in node:

            value = alpha_beta(child, alpha, beta, True)

            bestValue = min(bestValue, value)

            # Update beta
            beta = min(beta, bestValue)

            # Check pruning condition
            if beta <= alpha:
                print("Pruning remaining branch")
                break

        return bestValue


# Game tree
tree = [
    [[3, 5], [6, 9]],
    [[1, 2], [0, -1]]
]

# Initial call
result = alpha_beta(
    tree,
    float('-inf'),
    float('inf'),
    True
)

print("Optimal value:", result)
