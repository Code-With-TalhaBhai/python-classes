# For DAG
from collections import defaultdict


# [To,From,Weight]
edge_list = [[0,1,5],[0,2,3],[1,2,2],[1,3,6],[2,3,7],[2,4,4],[2,5,2],[3,4,-1],[4,5,-2]]


adjacency_list = defaultdict(list)
for u,v,w in edge_list:
    adjacency_list[u].append((v,w))
    adjacency_list[v]

# print(adjacency_list)

# topological sort
def tp_sort(adjacency_list):
    visited = set()
    sorting = []

    def dfs(node):
        visited.add(node)

        for neighbour in adjacency_list[node]:
            if neighbour[0] not in visited:
                dfs(neighbour[0])
            
        sorting.insert(0,node)

    for node in adjacency_list:
        if node not in visited:
            dfs(node)
    return sorting


topological_sort = tp_sort(adjacency_list)
# print(topological_sort)


def shortestPath(src,topological_sort):
    shortest_paths = {i:float("inf") for i in topological_sort}
    shortest_paths[src] = 0

    # for tackling source-node
    for node in topological_sort:
        if adjacency_list[node] != float("inf"):
            # for neighbour in adjacency_list[node]:
            #     if shortest_paths[node] + neighbour[1] < shortest_paths[neighbour[0]]:
            #         shortest_paths[neighbour[0]] = shortest_paths[node] + neighbour[1]
            for neighbour,weight in adjacency_list[node]:
                if shortest_paths[node] + weight < shortest_paths[neighbour]:
                    shortest_paths[neighbour] = shortest_paths[node] + weight


    return shortest_paths




print(shortestPath(1,topological_sort))


