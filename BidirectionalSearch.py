def bidirectional_bfs(graph, start, goal):
    # Initialize the forward and backward frontiers
    forward_frontier = [start]
    backward_frontier = [goal]
    
    # Initialize the explored sets for the forward and backward searches
    forward_explored = set([start])
    backward_explored = set([goal])
    
    # Initialize the parent dictionaries for the forward and backward searches
    forward_parent = {start: None}
    backward_parent = {goal: None}
    
    # Loop until the frontiers meet
    while forward_frontier and backward_frontier:
        # Check if any nodes in the forward frontier are in the backward explored set
        for node in forward_frontier:
            if node in backward_explored:
                # We have a path!
                path = path_to_root(forward_parent, backward_parent, node)
                return path
        
        # Expand the next node in the forward frontier
        next_frontier = set()
        for node in forward_frontier:
            for neighbor in graph[node]:
                if neighbor not in forward_explored:
                    forward_explored.add(neighbor)
                    forward_parent[neighbor] = node
                    next_frontier.add(neighbor)
        forward_frontier = list(next_frontier)
        
        # Check if any nodes in the backward frontier are in the forward explored set
        for node in backward_frontier:
            if node in forward_explored:
                # We have a path!
                path = path_to_root(forward_parent, backward_parent, node)
                return path
        
        # Expand the next node in the backward frontier
        next_frontier = set()
        for node in backward_frontier:
            for neighbor in graph[node]:
                if neighbor not in backward_explored:
                    backward_explored.add(neighbor)
                    backward_parent[neighbor] = node
                    next_frontier.add(neighbor)
        backward_frontier = list(next_frontier)
    
    # If we reach this point, then there is no path from start to goal
    return None
    
def path_to_root(forward_parent, backward_parent, meeting_node):
    # Construct the path from start to meeting node
    path = []
    current = meeting_node
    while current is not None:
        path.append(current)
        current = forward_parent[current]
    path.reverse()
    
    # Construct the path from meeting node to goal
    current = backward_parent[meeting_node]
    while current is not None:
        path.append(current)
        current = backward_parent[current]
    
    return path

        