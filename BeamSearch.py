def bubble_sortb(lst, key=None, k=None):
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if key(lst[j]) > key(lst[j + 1]):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst[0:k]
        

def beam_search(graph, heuristic, k):
    # Get the keys as a list
    keys_list = list(graph.keys())

    # Access the key at a specific index
    node = keys_list[0]
    visited = []
    beam = [(node, 0)]
    while beam:
        beam = bubble_sortb(beam, key=lambda x: x[1], k=k)
        for i in range(min(k, len(beam))):
            node, _ = beam.pop(0)
            if node not in visited:
                visited.append(node)
                if node in heuristic and heuristic[node] == 0:
                    return visited
                beam.extend((neighbor, heuristic[neighbor]) for neighbor in graph[node])
    return visited

