class Graph:
    def breadth_first_search(self, v):
        self.graph = dict(sorted(self.graph.items()))
        visit, i = [], 0
        visit.append(v)
        while i < len(visit):
            node = visit[i]
            connections = sorted(self.graph[node])
            for item in connections:
                if item not in visit:
                    visit.append(item)
            i += 1
        return visit

    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result
