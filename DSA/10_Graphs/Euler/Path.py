# A path is an eulerian-path which covers all the edges exactly one time:

# For Code
# 1. All `non-zero` degree vertices should be connected i.e Single-Component
# 2. Either zero or two vertices have odd degree

from collections import defaultdict


edge_list = [(0,1),(0,2),(0,3),(1,2),(3,4)]
adjacency_list = defaultdict(list)
for u,v in edge_list:
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)



def check_euler_path(graph):
    degrees = defaultdict(int)
    visited = set()

    # degrees = {i:len(graph[i]) for i in graph}
    # print(degrees)

    odd_vertices = 0
    for i in graph:
        if len(graph[i]) % 2 == 1:
            odd_vertices += 1

    if odd_vertices == 0 or odd_vertices == 2:
        print("Eulerian Path")
    else:
        print("Not a Eulerian Path")    


check_euler_path(adjacency_list)