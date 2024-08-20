from collections import defaultdict

def tarjan(graph):
    index = 0
    stack = []
    indices = {}
    lowlink = {}
    sccs = []

    def strongconnect(v):
        nonlocal index
        indices[v] = index
        lowlink[v] = index
        index += 1
        stack.append(v)

        for w in graph[v]:
            if w not in indices:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif w in stack:
                lowlink[v] = min(lowlink[v], indices[w])

        if lowlink[v] == indices[v]:
            scc = []
            while True:
                w = stack.pop()
                scc.append(w)
                if w == v:
                    break
            sccs.append(scc)

    for v in dict(graph):
        if v not in indices:
            strongconnect(v)

    return sccs



edge_list = [(0,1),(1,2),(2,0),(2,3),(3,4),(4,5),(4,7),(5,6),(6,4),(6,7)]
adjacency_list = defaultdict(list)
for u,v in edge_list:
    adjacency_list[u].append(v)

print(tarjan(adjacency_list))