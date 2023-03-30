############# deep recursion from left
def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.append(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)
            
############ deep iteractive from right, strnage, but cant find better..
def dfs_iterative(graph, start):
    stack, path = [start], []
    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)
    return path

visited = []
dict = {1: [2], 0: [1, 2], 2: [], 4: [5], 3: [4], 5: []}
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : [],
  'D' : [],
  'E' : []
}
node = 3
dfs(visited, graph, 'I')
dfs_iterative(graph, 'A')
############

############  wide
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        s = queue.pop(0) 
        print (s, end = " ") 
        
        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
            
visited = []
queue = []

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : [],
  'D' : [],
  'E' : []
}

bfs(visited, graph, 'I')