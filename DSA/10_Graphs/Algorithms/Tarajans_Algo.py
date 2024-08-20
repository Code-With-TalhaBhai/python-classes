from collections import defaultdict


# edge_list = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,3]]
edge_list = [(0,1),(1,2),(2,0),(2,3),(3,4),(4,5),(4,7),(5,6),(6,4),(6,7)]



adjacency_list = defaultdict(list)
for u,v in edge_list:
    adjacency_list[u].append(v)
    adjacency_list[v]



def dfs(node,adjacency_list,time,visited,disc,low,count,stack,sccs):
    visited.add(node)
    disc[node] = time
    low[node] = time
    stack.append(node)
    time += 1

    for neighbour in adjacency_list[node]:
        if neighbour not in visited:
            dfs(neighbour,adjacency_list,time,visited,disc,low,count,stack,sccs)
        low[node] = min(low[node],low[neighbour])


    if disc[node] == low[node]:
        count[0] += 1
        scc = []
        while True:
            component = stack.pop()
            scc.append(component)
            if component == node:
                break
        sccs.append(scc)


def tarjans_algo(adjacency_list):
    visited = set()
    n = len(adjacency_list)
    disc =  [0]*n  #discovery time of node
    low = [0]*n #lower(minimum) discovery time that can be reached by current node
    count = [0]
    stack = []
    sccs = []

    # print(adjacency_list)
    for node in adjacency_list:
        if node not in visited:
            print('working',node)
            dfs(node,adjacency_list,0,visited,disc,low,count,stack,sccs)

    
    return sccs
    # For total numnber of strongly connected components
    # return count[0] 


print(tarjans_algo(adjacency_list))