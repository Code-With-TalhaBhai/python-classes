from collections import defaultdict

# A bridge is such edge which removal increase the number of components
# A single wire failure which disconnects the graph

# edge_list = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,2]]
edge_list = [[0,1],[0,4],[1,2],[1,3],[2,5],[3,4],[5,6],[5,7],[6,7],[7,8],[8,9],[8,10],[9,10]]
# edge_list = [[0,1],[0,3],[1,2],[2,4],[2,5],[4,3],[5,6],[6,7],[6,8],[7,8],[8,9],[9,10],[9,11],[10,12],[11,12]]

adjacency_list = defaultdict(list)
for u,v in edge_list:
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)
# print(adjacency_list)


def find_bridge(adjacency_list):
    bridges = []
    disc = {}
    low = {}
    parent = {0:-1}
    visited = set()
    time = [0]

    def bridge_dfs1(node):
        visited.add(node)
        disc[node] = time[0]
        low[node] = time[0]

        # for neighbour in adjacency_list[node]:
        #     if parent[node] == neighbour:
        #         continue

        #     if neighbour not in visited:
        #         parent[neighbour] = node
        #         time[0] += 1
        #         bridge_dfs1(neighbour)

        #     low[node] = min(low[node],low[neighbour])

        #     if disc[node] < low[neighbour]:
        #         bridges.append((node,neighbour))


    def bridge_dfs2(node):
        visited.add(node)
        disc[node] = time[0]
        low[node] = time[0]

        for neighbour in adjacency_list[node]:
            if parent[node] == neighbour:
                continue
            elif neighbour in visited:
                low[node] = min(low[node],low[neighbour])
            else:
                parent[neighbour] = node
                time[0] += 1
                bridge_dfs2(neighbour)
                low[node] = min(low[node],low[neighbour])
                if disc[node] < low[neighbour]:
                    bridges.append((node,neighbour))


    # both same
    # bridge_dfs1(0) # by me
    bridge_dfs2(0)

    # print(disc)
    # print(low)
    # print(parent)
    return bridges

print(find_bridge(adjacency_list))