from collections import defaultdict,deque
from operator import ne

# edge_list = [[1,2],[1,3],[2,4],[3,4],[4,5],[4,6],[5,6]]
edge_list = [[0,2],[0,3],[1,3],[1,4],[2,3]]

# vertices
adjacency_list = defaultdict(list)


for u,v in edge_list:
    adjacency_list[u].append(v)
    adjacency_list[v]
# print(adjacency_list)

indegree = {i:0 for i in adjacency_list}

# creating-indegree
for node in adjacency_list:
    for neighbour in adjacency_list[node]:
        indegree[neighbour] += 1

# print(indegree)


# dq = deque()
# for node in indegree:
#     if indegree[node] == 0:
#         dq.append(node)

# Same as above, short
dq = deque([node for node in indegree if indegree[node] == 0])
# print(dq)

topological_sort = []

while dq:
    element = dq.popleft()
    topological_sort.append(element)

    for neighbour in adjacency_list[element]:
        indegree[neighbour] -= 1

        if indegree[neighbour] == 0:
            dq.append(neighbour)


# additional
# if len(topological_sort) == len(adjacency_list):
#     print(topological_sort)
# else:
#     print("graph has cycle")

print(topological_sort)

