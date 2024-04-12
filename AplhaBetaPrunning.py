def alpha_beta_minimax(values, depth, alpha, beta, maximizing_player):
    if depth == 0 or len(values) == 0:
        return max(values) if maximizing_player else min(values)

    if maximizing_player:
        value = float('-inf')
        for child in get_children(values):
            value = max(value, alpha_beta_minimax(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value

    else:
        value = float('inf')
        for child in get_children(values):
            value = min(value, alpha_beta_minimax(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value


def get_children(values):
    # Return a list of all possible child states from the given state
    children = []
    for i in range(len(values)):
        child = values[:i] + values[i+1:]
        children.append(child)
    return children