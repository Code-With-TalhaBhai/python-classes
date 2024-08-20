from collections import defaultdict

# Kosarajus' Algorithm
# 1. Perform DFS
# 2. Perform Transpose
# 3. Each succesful DFS gives you single `Strongly Connected Component`

edge_list = [(0,1),(1,2),(2,0),(2,3),(3,4),(4,5),(4,7),(5,6),(6,4),(6,7)]


adjacency_list = defaultdict(list)
for u,v in edge_list:
    adjacency_list[u].append(v)

def dfs(node,adjacency_list,visited,scc,stack=None):
    visited.add(node)
    if stack is not None: # for first dfs
        for neighbour in adjacency_list[node]:
            if neighbour not in visited:
                dfs(neighbour,adjacency_list,visited,scc,stack)
        stack.append(node)
    else: # for second dfs with transpose adjacency_list
        # print(node,end=" ")
        scc.append(node)
        for neighbour in adjacency_list[node]:
            if neighbour not in visited:
                dfs(neighbour,adjacency_list,visited,scc)


def transpose(adjacency_list):
    tranpose_list = defaultdict(list)

    for node in adjacency_list:
        for neighbour in adjacency_list[node]:
            tranpose_list[neighbour].append(node)

    return tranpose_list


def find_sccs(adjacency_list):
    stack = []
    visited = set()
    sccs = []
    for node in dict(adjacency_list):
        if node not in visited:
            dfs(node,adjacency_list,visited,[],stack)
            

    transpose_adjacency_list = transpose(adjacency_list)
    visited.clear()
    
    while stack:
        node = stack.pop()
        if node not in visited:
            scc = []
            dfs(node,transpose_adjacency_list,visited,scc)
            sccs.append(scc)

    return sccs

print("Strongly Connected Components in the graph:")
print(find_sccs(adjacency_list))
