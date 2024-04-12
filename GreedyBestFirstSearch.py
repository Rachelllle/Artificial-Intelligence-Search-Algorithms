from queue import PriorityQueue

def greedy_best_first_search(graph, start, goal, heuristic):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next_node in graph[current]:
            if next_node not in came_from:
                priority = heuristic(next_node, goal)
                frontier.put(next_node, priority)
                came_from[next_node] = current

    path = [goal]
    current = goal
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()

    return path
