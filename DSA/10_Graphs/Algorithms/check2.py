
adjacency_list = {0:[1,3],1:[2,5],2:[3],3:[0],5:[]}


def find(graph):
    desc = {}
    low = {}
    visited = set()

    def dfs(node,time):
        visited.add(node)
        # print('working')
        desc[node] = time[0]
        low[node] = time[0]
        # time += 1

        for neighbour in adjacency_list[node]:
            if neighbour not in visited:
                time[0] += 1
                dfs(neighbour,time)

    time = [0]
    dfs(0,time)

    print(desc)
    print(low)


find(adjacency_list)