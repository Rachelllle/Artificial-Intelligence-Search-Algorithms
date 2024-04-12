import random

def random_restart_hill_climbing(graph, heuristic, num_restarts):
    best_path = []
    best_final_state = None
    for _ in range(num_restarts):
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
        if len(path) > len(best_path):
            best_path = path
            best_final_state = current_node
    return best_path, best_final_state

