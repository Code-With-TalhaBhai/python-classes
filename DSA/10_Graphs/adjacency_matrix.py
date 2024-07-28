n = 8
edge_list = [[0,1],[0,3],[1,2],[3,4],[3,6],[3,7],[4,2],[4,5],[5,2]]


adjacency_matrix = []

# for i in range(n):
#     adjacency_matrix.append([])
#     for j in range(n):
#         adjacency_matrix[i].append(0)

# Constructing Adjacency Matrix
for i in range(n):
    adjacency_matrix.append([0]*n)


for v,e in edge_list:
    adjacency_matrix[v][e] = 1
print(adjacency_matrix)
