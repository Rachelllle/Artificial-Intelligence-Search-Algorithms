def depth_limited( graph, startnode, goalnode, l): #function for BFS
  visited = [] # List for visited nodes.
  stack = []     #Initialize a stack
  node=startnode
  stack.append(startnode)
  i=0
  while len(stack) > 0 and i<=l :          # Creating loop to visit each node
    node=stack.pop()
    visited.append(node)
    if(node==goalnode):
      return visited
    neighbors=graph[node]
    for neighbor in neighbors:
      if neighbor not in visited:
        stack.append(neighbor)
    i+=1
  return visited








