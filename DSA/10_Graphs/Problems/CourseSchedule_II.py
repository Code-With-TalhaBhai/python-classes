from collections import defaultdict, deque

def canFinish(numCourses,prerequisites):
    from collections import defaultdict,deque
    if not prerequisites:
        return list(range(numCourses-1,-1,-1)) 

    topological_sort = []
    adjacency_list = defaultdict(list)
    indegrees = defaultdict(int)
    for u,v in prerequisites:
        adjacency_list[v].append(u)
        adjacency_list[u] 
        indegrees[u] += 1 
        

    # Using BFS(Kahn's Algorithm)
    # dq = deque([i for i in range(numCourses) if indegrees[i] == 0])
    # while dq:
    #     node = dq.popleft()
    #     topological_sort.append(node)

    #     for neighbour in adjacency_list[node]:
    #         indegrees[neighbour] -= 1

    #         if indegrees[neighbour] == 0:
    #             dq.append(neighbour)

    # if len(topological_sort) == len(adjacency_list):
    #     return topological_sort
    # else:
    #     return []



    # Using DFS
    visited = set()
    cycle = set()

    def dfs(node):
        visited.add(node)
        cycle.add(node)

        for neighbour in adjacency_list[node]:
            if neighbour not in visited:
                if dfs(neighbour):
                    return True
            elif neighbour in cycle:
                return True
            
        cycle.remove(node)
        topological_sort.insert(0,node)
        return False

    for i in range(numCourses):
        if i not in visited:
            if dfs(i):
                return []
        
    return topological_sort



prerequisites1 = [[1,0]]
prerequisites2 = [[1,0],[2,0],[3,1],[3,2]]
prerequisites3 = []
prerequisites4 = [[3,0],[0,1]]
prerequisites5 = [[1,0]]


print(canFinish(2,prerequisites1))
print(canFinish(4,prerequisites2))
print(canFinish(1,prerequisites3))
print(canFinish(3,prerequisites4))
print(canFinish(3,prerequisites5))


