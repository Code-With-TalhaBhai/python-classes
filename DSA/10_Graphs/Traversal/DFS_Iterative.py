from collections import defaultdict

edge_list = [[0,1],[0,3],[1,2],[3,4],[3,6],[3,7],[4,2],[4,5],[5,2]]


# Constructing Adjacency List
adjacency_list = defaultdict(list)
for v,e in edge_list:
    adjacency_list[v].append(e)



# Iterative DFS with `Stack` - O(V + E)
# Stack is used for `DFS_Iterative`
def dfs_iterative(stack):
    
   while stack:
       node = stack.pop()
       print(node)

       for neighbour in adjacency_list[node]:
    #    for neighbour in reversed(adjacency_list[node]): # for sorted
           if neighbour not in seen:
            seen.add(neighbour)
            stack.append(neighbour) 


source = 0
seen = set()
seen.add(source)

stack = []
stack.append(source)
dfs_iterative(stack)
print(seen)