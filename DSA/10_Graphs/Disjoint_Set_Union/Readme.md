# DSU
A ***Disjoint Set Union (DSU)***, also known as Union-Find or Merge-Find Set, is a data structure that keeps track of a partition of a set into disjoint (non-overlapping) subsets. It supports two main operations efficiently:

1. ***Find***: Determine which subset a particular element is in. This can be used for determining if two elements are in the same subset.
2. ***Union***: Join two subsets into a single subset.


## Key Concepts
+ ***Union by Rank:*** When performing a union operation, the smaller tree (by rank) is added under the root of the deeper tree to keep the resulting tree shallow.
+ ***Path Compression:*** During the Find operation, the tree is flattened by making every node point directly to the root, which speeds up future operations.


## Usage 
+ ***Kruskal's Algorithm:*** To find the minimum spanning tree of the graph
+ ***Cycle Detection:*** In an undirected graph
+ ***Network connectivity:*** To determine connectivity between two nodes