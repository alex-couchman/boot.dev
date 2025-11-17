class Graph:
    def adjacent_nodes(self, node):
        if node in self.graph:
            return self.graph[node]

    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = {v}
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = {u}


import os
import json

if __name__ == "__main__":
    edges = [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
        ]
    graph = Graph()
    for edge in edges:
        u, v = edge[0], edge[1]
        graph.add_edge(u, v)

    print("{")
    for key in graph.graph.keys():
        print(f"\t{key} : {graph.graph[key]}")
    print("}")

    print(graph.adjacent_nodes(6))
