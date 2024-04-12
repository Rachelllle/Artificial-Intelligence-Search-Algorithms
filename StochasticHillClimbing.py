import random

def stochastic_hill_climbing(graph, heuristic):
    current_node = random.choice(list(graph.keys()))
    path = [current_node]
    while True:
        neighbors = graph[current_node]
        best_heuristic = heuristic[current_node]
        best_neighbors = [current_node]
        for neighbor in neighbors:
            neighbor_heuristic = heuristic[neighbor]
            if neighbor_heuristic < best_heuristic:
                best_heuristic = neighbor_heuristic
                best_neighbors = [neighbor]
            elif neighbor_heuristic == best_heuristic:
                best_neighbors.append(neighbor)
        if current_node == best_neighbors[0]:
            break
        current_node = random.choice(best_neighbors)
        path.append(current_node)
    return path, current_node
