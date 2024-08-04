from collections import defaultdict

# edge_list = [[1,2],[1,3],[2,4],[3,4],[4,5],[4,6],[5,6]]
edge_list = [[0,2],[0,3],[1,3],[1,4],[2,3]]

adjacency_list = defaultdict(list)

for u,v in edge_list:
    adjacency_list[u].append(v)
print(adjacency_list)



def toplogical_sort(adjacency_list,node,visited,stack):
    visited.add(node)

    for neighbour in adjacency_list[node]:
        if neighbour not in visited:
            toplogical_sort(adjacency_list,neighbour,visited,stack)

    stack.insert(0,node)
    return stack



def check():
    visited = set()
    stack = []
    for node in dict(adjacency_list):
        if node not in visited:
            toplogical_sort(adjacency_list,node,visited,stack)
    return stack

print(check())
