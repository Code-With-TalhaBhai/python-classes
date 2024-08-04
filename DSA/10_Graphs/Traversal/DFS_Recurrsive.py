from collections import defaultdict

edge_list = [[0,1],[0,3],[1,2],[3,4],[3,6],[3,7],[4,2],[4,5],[5,2]]


# Constructing Adjacency List
adjacency_list = defaultdict(list)
for v,e in edge_list:
    adjacency_list[v].append(e)
    # Uncomment if the graph is undirected
    # adjacency_list[e].append(v)


print(dict(adjacency_list)) 
# print(adjacency_list[0])




# DFS with Recurrsion - O(V+E) where V is the number of nodes and E is the number of edges
def dfs_recurrsive(adjacency_list,node,visited=None):
    if not visited:
        visited = set()

    if node not in visited:
        print(node)
        visited.add(node)

        for neighbour in adjacency_list[node]:
            if neighbour not in visited:
                dfs_recurrsive(adjacency_list,neighbour,visited)

    # print(node)
    # for neighbour in adjacency_list[node]:
    #     if neighbour not in visited:
    #         visited.add(neighbour)
    #         dfs_recurrsive(adjacency_list,neighbour,visited)


# source = 0
# seen = set()
# seen.add(source)
# seen = []
# seen.append(source)
dfs_recurrsive(adjacency_list,0)
# print(seen)