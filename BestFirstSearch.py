from queue import PriorityQueue

def heuristic(node):
    distances = {
        'A': 6,
        'B': 5,
        'C': 4,
        'D': 5,
        'E': 3,
        'F': 0,
    }
    return distances[node]

def best_first_search(graph, start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristic(start), [start]))
    
    while not pq.empty():
        node_path = pq.get()[1]
        node = node_path[-1]
        if node == goal:
            return node_path
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                neighbor_path = node_path + [neighbor]
                pq.put((heuristic(neighbor), neighbor_path))
                
    return None

