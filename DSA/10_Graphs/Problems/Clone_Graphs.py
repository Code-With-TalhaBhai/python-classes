

from collections import defaultdict, deque
import queue
from tkinter import NO


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


adjList = {
    1: [2,4],
    2: [1,3],
    3: [2,4],
    4: [1,3]
}


# nodes_list = {}
def clone_graphs(node):
    if not node:
        return None
    
    old_to_new = {}

    # DFS -> More optimised
    # def dfs(node):
    #     visited.add(node)
    #     # More optimised
    #     if node.val in old_to_new:
    #         return old_to_new[node.val]
    #     new_node = Node(node.val)
    #     old_to_new[node.val] = new_node


    #     # if node in old_to_new:
    #     #     return old_to_new[node]
    #     # new_node = Node(node.val)
    #     # old_to_new[node] = new_node


    #     for neighbours in node.neighbors:
    #         new_node.neighbors.append(dfs(neighbours))
    #     return new_node
    # return dfs(node)


    # BFS
    q = deque([node])
    visited = set()
    start = node
    visited.add(node)

    while q:
        node = q.popleft()
        old_to_new[node] = Node(node.val)

        for neighbours in node.neighbors:
            if neighbours not in visited:
                visited.add(neighbours)
                q.append(neighbours)


    for nodes in old_to_new:
        for neighbours in nodes.neighbors:
            res_node = old_to_new[nodes]
            nei_node = old_to_new[neighbours]
            res_node.neighbors.append(nei_node)
    return old_to_new[start]  




node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2,node4]
node2.neighbors = [node1,node3]
node3.neighbors = [node2,node4]
node4.neighbors = [node1,node3]

clone_graphs(node1)
