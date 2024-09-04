from collections import defaultdict


# edge_list = [(0,1,3),(0,3,5),(1,0,2),(1,3,8),(2,1,1),(3,2,2)]
edge_list = [(0,3,4),(0,2,2),(1,0,3),(1,3,10),(2,3,1),(3,0,6),(3,1,4)]
edge_list = [[0,1,3],[1,2,5],[2,0,-6]] #  with negative weight



adjacency_list = defaultdict(list)
for u,v,w in edge_list:
    adjacency_list[u].append((v,w))

n = len(adjacency_list)
matrix = [[float("inf")]*n for _ in range(n)]


for row in adjacency_list:
    for col in adjacency_list:
        if row == col:
            matrix[row][col] = 0
            continue
        for item in adjacency_list[row]:
            if item[0] == col:
                matrix[row][col] = item[1]

# print(matrix)

for item in adjacency_list:
    for row in adjacency_list:
        # for optimization but can be skipped - must be skipped if it has negative weights with not negative cycle
        if row == item:
            continue
        for col in adjacency_list:
            # for optimization but can be skipped - must be skipped if it has negative weights with not negative cycle
            if row == col or col == item:
                continue

            # if matrix[row][item] + matrix[item][col] < matrix[row][col]:
            #     matrix[row][col] = matrix[row][item] + matrix[item][col]
            matrix[row][col] = min(matrix[row][col],(matrix[row][item] + matrix[item][col]))


print(matrix)