from collections import defaultdict

edge_list = [[0,1],[0,3],[1,2],[3,4],[3,6],[3,7],[4,2],[4,5],[5,2]]


# Constructing Adjacency List
adjacency_list = defaultdict(list)
for v,e in edge_list:
    adjacency_list[v].append(e)


print(dict(adjacency_list)) 


