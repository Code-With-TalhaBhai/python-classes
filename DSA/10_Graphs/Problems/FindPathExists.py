from collections import defaultdict, deque

# leetcode 1971
def validPath(edges, source: int, destination: int) -> bool:

    adjacency_list = defaultdict(list)
    for u,v in edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    visited = set()

    # Through dfs
    # def dfs(node):
    #     visited.add(node)
    #     if node == destination:
    #         return True
        

    #     for neighbour in adjacency_list[node]:
    #         if neighbour not in visited:
    #             if dfs(neighbour):
    #                 return True
    #     return False
        
    # if dfs(source):
    #     return True
    # else:
    #     return False


    # Through bfs(More Optimised in this code)
    visited.add(source)
    dq = deque()
    dq.append(source)
    while dq:
        node = dq.popleft()
        if node == destination:
            return True

        for neighbour in adjacency_list[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                dq.append(neighbour)

    return False


edges1 = [[0,1],[1,2],[2,0]]
edges2 = [[0,1],[0,2],[3,5],[5,4],[4,3]]

print(validPath(edges1,0,2))
print(validPath(edges1,0,5))