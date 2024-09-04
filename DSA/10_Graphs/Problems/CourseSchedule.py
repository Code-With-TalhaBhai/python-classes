# leetcode 207
from collections import defaultdict, deque

def canFinish(prerequisites):
    adjacency_list = defaultdict(list)
    for u,v in prerequisites:
        adjacency_list[u].append(v)
        adjacency_list[v]


    # visited = set()
    # dfs_visited = set()
    # # Through dfs
    # def dfs(node):
    #     # print(node)
    #     visited.add(node)
    #     dfs_visited.add(node)

    #     for neighbour in adjacency_list[node]:
    #         if neighbour not in visited:
    #             if dfs(neighbour):
    #                 return True
    #         elif neighbour in dfs_visited:
    #             return True
            
    #     dfs_visited.remove(node)
    #     return False


    # for node in dict(adjacency_list):
    #     if node not in visited:
    #         if dfs(node):
    #             return False
    # return True


    # Through-BFS(Topological Sort (Kahn's Algorithm))
    indegrees = {i:0 for i in adjacency_list}
    for node in adjacency_list:
        for neighbour in adjacency_list[node]:
            indegrees[neighbour] += 1


    dq = deque([indegree for indegree in indegrees if indegrees[indegree] == 0])
    topological_sort = []

    while dq:
        node = dq.popleft()
        topological_sort.append(node)

        for neighbour in adjacency_list[node]:
            indegrees[neighbour] -= 1

            if indegrees[neighbour] == 0:
                dq.append(neighbour)

    if len(adjacency_list) == len(topological_sort):
        return True
    else:
        return False



prerequisites1 = [[1,0]]
prerequisites2 = [[1,0],[0,1]]
prerequisites3 = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
print(canFinish(prerequisites1))
print(canFinish(prerequisites2))
print(canFinish(prerequisites3))
