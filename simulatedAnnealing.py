import random
from numpy import asarray, exp
from numpy.random import randn, rand, seed

def simAnnealing(graph, heuristic,iterations, temperature):
    current_node=random.choice(list(graph.keys()))


    current_heuristic=heuristic[current_node]
    path=[current_node]

    for i in range(iterations):
        neighbors=graph[current_node]
        next_node=random.choice(list(neighbors.keys()))
        next_heuristic=heuristic[next_node]

        if next_heuristic < current_heuristic :
            current_node=next_node
            current_heuristic=next_heuristic

        difference = next_heuristic - current_heuristic
        t = float(temperature) / float(i + 1)

        mac = exp(-difference / t)
            # check whether the new point is acceptable
        r=rand()
        if difference < 0 or r < mac:
            current_node = next_node
            current_heuristic = next_heuristic
            path.append(current_node)

    return path, current_node