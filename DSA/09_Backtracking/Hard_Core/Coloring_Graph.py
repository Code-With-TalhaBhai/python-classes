# leetcode 1042
from collections import defaultdict

# working
def m_coloring(edge_list,m):
    adjacency_list = defaultdict(list)
    colors = {}
    for u,v in edge_list:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
        colors[u] = -1
        colors[v] = -1


    visited = set()

    def valid(node,color):
        for neighbour in adjacency_list[node]:
            if neighbour not in visited:
                continue
            elif colors[neighbour] == color:
                return False
        return True

    def dfs(node):
        if node not in visited:
            visited.add(node)

            for neighbour in adjacency_list[node]:
                if neighbour not in visited:
                    for i in range(m):
                        if valid(node,i):
                            dfs(neighbour)


    return dfs(0)







edge_list1 = [(0,1),(1,2),(2,3),(3,0),(0,2)]
print(m_coloring(edge_list1,3))

edge_list2 = [(0,1),(1,2),(0,2)]
print(m_coloring(edge_list2,2))

# edge_list1 = [(0,1),(0,2),(0,3),(1,2),(2,3)]
# edge_list2 = [(0,1),(0,4),(0,5),(0,10),(1,2),(1,3),(1,4),(2,3),(3,4),(3,5),(3,8),(3,9),(5,6),(5,7),(6,7),(8,9),(10,11),(10,12),(11,12)]
# edge_list3 = [(0,1),(0,2),(1,2)]
# edge_list4 = [[1,2],[2,3],[3,1]]
