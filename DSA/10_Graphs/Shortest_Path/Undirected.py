from collections import defaultdict,deque

# edges=[[0,1],[0,3],[3,4],[4,5],[5,6],[1,2],[2,6],[6,7],[7,8],[6,8]] 
edges = [[1,2],[1,3],[1,4],[2,5],[3,8],[4,6],[5,8],[6,7],[7,8]]


adjacency_list = defaultdict(list)


for u,v in edges:
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)
# print(adjacency_list)


def shortest_path(src,dest):
    visited = set()
    parent = {}
    dq = deque([src])
    visited.add(src)
    parent[src] = -1


    while dq:
        element = dq.popleft()

        # optional(me)
        # if element == dest:
        #     break

        for neighbour in adjacency_list[element]:
            if neighbour not in visited:
                visited.add(neighbour)
                dq.append(neighbour)
                parent[neighbour] = element


    # path = [dest]
    # while parent[dest] != -1:
    #     dest = parent[dest]
    #     path.append(dest)
    path = []
    while dest != -1:
        path.append(dest)
        dest = parent[dest]

    path.reverse()
    return path

print(shortest_path(1,8))