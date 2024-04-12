import heapq

def uniform_cost_search(graph, start, goal):
    frontier = [(0, start)]
    explored = set()
    parent = {start: None}
    
    while frontier:
        # Pop the node with the lowest cost from the frontier
        cost, node = heapq.heappop(frontier)
        
        if node == goal:
            # We have found a path!
            path = path_to_root(parent, goal)
            return cost, path
        
        explored.add(node)
        
        for neighbor, neighbor_cost in graph[node]:
            if neighbor not in explored:
                # Compute the total cost of the path to the neighbor
                total_cost = cost + neighbor_cost
                
                # If the neighbor is already in the frontier, update its cost if necessary
                for i, (old_cost, old_node) in enumerate(frontier):
                    if old_node == neighbor and total_cost < old_cost:
                        frontier[i] = (total_cost, neighbor)
                        heapq.heapify(frontier)
                        parent[neighbor] = node
                        break
                else:
                    # Add the neighbor to the frontier
                    heapq.heappush(frontier, (total_cost, neighbor))
                    parent[neighbor] = node
    
    # If we reach this point, then there is no path from start to goal
    return None, None

def path_to_root(parent, node):
    path = []
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()
    return path



