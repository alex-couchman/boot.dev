class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, calls=2):
        if calls > 0:
            if u != v:
                if u not in self.graph:
                    self.graph[u] = set()
                current_set = self.graph[u]
                current_set.add(v)
            calls -= 1
            self.add_edge(v, u, calls=calls)

    # don't touch below this line

    def edge_exists(self, u, v):
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) and (u in self.graph[v])
        return False


import os
import json

if __name__ == "__main__":
    graph = Graph()
    my_dict = {}
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 5)
    graph.add_edge(2, 2)
    graph.add_edge(2, 3)
    graph.add_edge(2, 5)
    graph.add_edge(3, 1)

    print("{")
    for key in graph.graph.keys():
        print(f"\t{key} : {graph.graph[key]}")
    print("}")
