from collections import defaultdict,deque


# Using Kahn's Algorithm
edge_list = [[1,2],[2,3],[2,4],[3,7],[3,8],[4,5],[5,6],[6,4],[8,7]] # Cyclic
# edge_list = [[1,2],[2,3],[2,4],[3,7],[3,8],[4,5],[4,6],[5,6],[8,7]] # Acyclic

adjacency_list = defaultdict(list)

for u,v in edge_list:
    adjacency_list[u].append(v)
    adjacency_list[v]


indegree = {i:0 for i in adjacency_list}

for node in adjacency_list:
    for neighbour in adjacency_list[node]:
        indegree[neighbour] += 1


dq = deque([node for node in indegree if indegree[node] == 0])
print(dq)

topological_sort = []
while dq:
    element = dq.popleft()
    topological_sort.append(element)

    for neighbour in adjacency_list[element]:
        indegree[neighbour] -= 1

        if indegree[neighbour] == 0:
            dq.append(neighbour)

print(adjacency_list)
print(topological_sort)
if len(topological_sort) == len(adjacency_list):
    print("False")
else:
    print("True")





