# DFS algorithm
def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    if start == goal:
        return visited

    for next in [node for node in graph[start] if node not in visited]:
        result = dfs(graph, next, goal, visited ) # Add next node to visited set
        if result is not None:
            return result
    return None


