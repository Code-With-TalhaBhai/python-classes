from collections import defaultdict

edge_list = [[1,2],[2,3],[2,4],[3,7],[3,8],[4,5],[5,6],[6,4],[8,7]]

adjacency_list = defaultdict(list)


for u,v in edge_list:
    adjacency_list[u].append(v)
# print(adjacency_list)



def dfs_cycle(adjacency_list,node,visited=None,DFS_visited=None):
    if not visited:
        visited = set()

    if not DFS_visited:
        DFS_visited = defaultdict(bool)

    if DFS_visited[node] == True:
        return True
    
    if node in visited:
        return False

    visited.add(node)
    DFS_visited[node] = True
    
    for neighbour in adjacency_list[node]:
        if dfs_cycle(adjacency_list,neighbour,visited,DFS_visited):
            return True

    DFS_visited[node] = False
    return False
    


print(dfs_cycle(adjacency_list,1)) # For Single Graph


# For disconnected graphs(sub-graphs)
def disconnected_cycle():
    visited = set()
    DFS_visited = defaultdict()
    for node in adjacency_list:
        if node not in visited:
            if dfs_cycle(adjacency_list,node,visited,DFS_visited):
                return True    
    return False


print(disconnected_cycle())
