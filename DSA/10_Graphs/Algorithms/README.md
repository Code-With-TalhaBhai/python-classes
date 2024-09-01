# Greedy Algorithm
Greedy algorithms are a type of algorithmic approach used in problem-solving where the algorithm makes a sequence of choices, each of which looks best at the moment (locally optimal) without considering the bigger picture (global optimality). The idea is to pick the best available option at each step with the hope that these local choices will lead to a globally optimal solution.

However, greedy algorithms do not always guarantee the best overall solution for every problem. They work well for specific types of problems where a globally optimal solution can be reached by following a series of locally optimal steps. Some classic examples where greedy algorithms are effective include:


**Digkstra's Algorithm:** For finding `Shortest Path` in directed graph with non-negative edge weights(Time-Complexity - E log V)

**Prim's Algorithm:** For finding `Minimum Spanning Tree`

**Kruskals Algorithm:** For finding `Minimum Spanning Tree`

**Kosarajus Algorithm:** For finding `Strongly Connected Component`

**Tarajan's Algorithm:** For finding `Strongly Connected Component`

**Bellman-Ford Algorithm:** For finding `Shortest Path` in directed graph with positive as well as negative edge weights. `Undirected graph with non-negative weight`(Time-Complexity - E.V)

**Floyd-Warshall Algorithm:** For finding `Multi-Source Shortest Path` in directed graph. Finding all nodes distance from all nodes


***Spanning-Tree:*** A spanning tree is a subgraph of an undirected graph that includes all the vertices of the original graph, connected with the minimum possible number of edges, and without forming any cycles. Essentially, a spanning tree "spans" all the vertices in the graph while ensuring there is exactly one path between any two vertices.

1. Contains All Vertices: A spanning tree includes every vertex in the original graph.
2. Minimum Edges: It has exactly 𝑉−1 edges, where 𝑉 is the number of vertices in the graph.
3. No Cycles: There are no cycles in a spanning tree, which means it is a type of acyclic subgraph.
4. Connected: A spanning tree is always connected, meaning there is a path between any pair of vertices.