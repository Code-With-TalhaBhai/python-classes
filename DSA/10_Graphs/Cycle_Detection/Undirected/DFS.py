# adjacency_list = {
#     1: [2],
#     2: [1,3],
#     3: [2],
#     4: [5],
#     5: [4,6,7],
#     6: [5,8],
#     7: [5,8],
#     8: [6,7,9],
#     9: [8]
# }

from collections import defaultdict,deque

edge_list = [[1,2],[2,3],[4,5],[5,6],[5,7],[6,8],[7,8],[8,9]]

adjacency_list = defaultdict(list)
for u,v in edge_list:
    adjacency_list[u].append(v)
    adjacency_list[v].append(u) # As it is undirected graph
print(adjacency_list)



def cycleUtil(node,visited,parent,adjacency_list):
    
    visited[node] = True
    for neighbour in adjacency_list[node]:
        if not visited[neighbour]:
            if cycleUtil(neighbour,visited,node,adjacency_list):
                return True
        elif neighbour != parent:
            return True
        
    return False


def isCycle(adjacency_list):
    visited = defaultdict(bool)
    for element in adjacency_list:
        if not visited[element]:
            if cycleUtil(element,visited,-1,adjacency_list):
                return True
        
    return False


print(isCycle(adjacency_list))
