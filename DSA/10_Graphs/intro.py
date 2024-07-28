# There are two ways of creating graphs

# 1. Adjacency List (Dictionary with key as `vertex` and edges`neighbour` are values)
# 2. Adjacency Matrix (2D List(Array) with index as vertex and elements are edges(neighbours))
# 3. Edge List (Mostly For Directed Graphs)

adjacency_list = {
    0: [1,3],
    1: [2],
    2: [],
    3: [4,6,7],
    4: [2,5],
    5: [2],
    6: [],
    7: []
}
adjacency_matrix = [
    [0,1,0,1,0,0,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,1,1],
    [0,0,1,0,1,0,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
    ]

edge_list = [[0,1],[0,3],[1,2],[3,4],[3,6],[3,7],[4,2],[4,5],[5,2]]
