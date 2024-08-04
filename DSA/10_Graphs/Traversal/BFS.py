# BFS(Queue) - O(V + E)
from collections import defaultdict,deque

edge_list = [[0,1],[0,3],[1,2],[3,4],[3,6],[3,7],[4,2],[4,5],[5,2]]


# Constructing Adjacency List
adjacency_list = defaultdict(list)
for v,e in edge_list:
    adjacency_list[v].append(e)



def bfs(adjacency_list):
    source = 0
    seen = set()
    seen.add(source)

    dq = deque()
    dq.append(source)

    
    while dq:
       node = dq.popleft()
       print(node)
       for neighbour in adjacency_list[node]:
           if neighbour not in seen:
               seen.add(neighbour)
               dq.append(neighbour) 


bfs(adjacency_list)
