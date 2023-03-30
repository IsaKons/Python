#Find all alone elements or separated secrors. return number of required new connections.

def dfs(visited, graph, node):
    visited[node] = node
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(visited, graph, neighbor)
    return visited

n = 4  #elements we have 1-2-3-4
connections = [[0,1],[0,2],[1,2]] #connections we have
           
sectors = -1
visited = [ [] for _ in range(n)]
graph = {key: [] for key in range(n)}

CountCon = len(connections)
if CountCon < n - 1:
    print(-1)

for k, v in connections:
    graph.setdefault(v, []).append(k)
    graph.setdefault(k, []).append(v)

for x in range(n):
    if not visited[x]:
        dfs(visited, graph, x)
        sectors += 1
print(sectors) #how much new connections we need or how much sectors we have -1