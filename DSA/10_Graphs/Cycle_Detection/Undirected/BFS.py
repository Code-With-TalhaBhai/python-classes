from collections import defaultdict,deque

edge_list = [[1,2],[2,3],[4,5],[5,6],[5,7],[6,8],[7,8],[8,9]]

adjacency_list = defaultdict(list)
for u,v in edge_list:
    adjacency_list[u].append(v)
    adjacency_list[v].append(u) # As it is undirected graph
# print(adjacency_list)


def cycleUtil(node,visited,adjacency_list):
    # parent_node = {node:-1}
    # visited[node] = True
    # dq = deque()
    # dq.append(node)

    # while dq:
    #     node_element = dq.popleft()
    #     for neighbour in adjacency_list[node_element]:
    #         if not visited[neighbour]:
    #             parent_node[neighbour] = node_element
    #             visited[neighbour] = True
    #             dq.append(neighbour)
    #         elif parent_node[node_element] != neighbour:
    #             return True
    # return False

    # 2nd way without extra parent dictionary
    visited[node] = True
    dq = deque()
    dq.append([node,-1])

    while dq:
        node_element,parent = dq.popleft()
        for neighbour in adjacency_list[node_element]:
            if not visited[neighbour]:
                visited[neighbour] = True
                dq.append([neighbour,node_element])
            elif neighbour != parent:
                return True
    return False



def isCycle(adjacency_list):
    visited = defaultdict(bool)
    # To handle disconnected behaviour
    for node in adjacency_list:
        if not visited[node]:
                # print(node)
            if cycleUtil(node,visited,adjacency_list):
                return True
        
    return False

print(isCycle(adjacency_list)) # Using BFS