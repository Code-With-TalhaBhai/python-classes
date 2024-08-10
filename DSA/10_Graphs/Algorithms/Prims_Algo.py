from collections import defaultdict

edge_list = [[0,1,2],[0,3,6],[1,2,3],[1,3,8],[1,4,5],[2,4,7]]


adjacency_list = defaultdict(list)
for u,v,w in edge_list:
    adjacency_list[u].append((v,w))
    adjacency_list[v].append((u,w))
# print(adjacency_list)


print(len(adjacency_list))
mst = set()