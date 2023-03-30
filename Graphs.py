from pprint import pprint

## From pair array to graph
def create_graph(pairs, empty_dict):
    for k, v in pairs:
        empty_dict.setdefault(v, [])   # add here .append(k) for two side!!!!
        empty_dict.setdefault(k, []).append(v)
    return empty_dict

empty_dict = {}
pairs = [('a', 'c'), ('b', 'c'), ('b', 'e'), ('c', 'a'), ('c', 'b'), ('c', 'd'), ('c', 'e'), ('d', 'c'), ('e', 'c'), ('e', 'f')]
graph = [[0,1],[0,2],[1,3],[3,4],[4,5]]
twopart = [[0,1],[0,2],[1,2],[3,4],[4,5]]

create_graph(twopart, empty_dict)

pprint(empty_dict)


# conversion of lists to dictionary
test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 4, 5]

print("Original key list is : " + str(test_keys))
print("Original value list is : " + str(test_values))

res = {}
for key in test_keys:
    for value in test_values:
        res[key] = value
        test_values.remove(value)
        break

print("Resultant dictionary is : " + str(res))


##### For Visualization!!
import networkx as nx
import matplotlib.pyplot as plt

class GraphVisualization:
    def __init__(self):
        self.visual = []
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()

# Driver code
G = GraphVisualization()
G.addEdge(0, 2)
G.addEdge(1, 2)
G.addEdge(1, 3)
G.addEdge(5, 3)
G.addEdge(3, 4)
G.addEdge(7, 7)
G.visualize()

#Example how to fill
for x in graph:
    if bool(graph[x]):
        for y in graph[x]:
            G.addEdge(x, y)