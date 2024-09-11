from collections import defaultdict

# `Node` whose removal increases the number of components
# Single point(node) of failure which breaks the network

# edge_list = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,2]]
# edge_list = [[0,1],[0,4],[1,2],[1,3],[2,5],[3,4],[5,6],[5,7],[6,7],[7,8],[8,9],[8,10],[9,10]]
# edge_list = [[0,1],[0,2],[1,3],[2,3],[3,4],[3,5],[4,6],[5,6]]
edge_list = [[0,1],[0,4],[1,2],[2,3],[4,5]] # Root as articulation point
 

adjacency_list = defaultdict(list)
for u,v in edge_list:
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)



def find_articulation_point(adjacency_list):
    articulation_points = []
    time = [0]
    disc = {}
    low = {}
    parent = {0:-1}
    visited = set()
    child = [0]


    # def dfs_articulation1(node):
    #     visited.add(node)
    #     disc[node] = time[0]
    #     low[node] = time[0]

    #     for neighbour in adjacency_list[node]:
    #         if parent[node] == neighbour:
    #             continue

    #         if neighbour not in visited:
    #             parent[neighbour] = node
    #             time[0] += 1
    #             dfs_articulation1(neighbour)

    #         if parent[neighbour] == node:
    #             low[node] = min(low[node],low[neighbour])
    #             if disc[node] <= low[neighbour] and parent[node] != -1:
    #                 print(node," ",neighbour)
    #                 articulation_points.append(node)
    #         else:
    #             low[node] = min(low[node],disc[neighbour])

    def dfs_articulation2(node):
        visited.add(node)
        disc[node] = time[0]
        low[node] = time[0]

        for neighbour in adjacency_list[node]:
            if parent[node] == neighbour:
                continue

            if neighbour in visited:
                low[node] = min(low[node],disc[neighbour])

            else:
                if node == 0: # for handling root condition as articulation point if it has more than one children and both are not connected to each other
                    child[0] += 1
                parent[neighbour] = node
                time[0] += 1
                dfs_articulation2(neighbour)
                low[node] = min(low[node],low[neighbour])
                if disc[node] <= low[neighbour] and (parent[node] != -1 or child[0] > 1):
                    articulation_points.append(node)

    # dfs_articulation1(0)
    dfs_articulation2(0)
    return articulation_points


print(find_articulation_point(adjacency_list))