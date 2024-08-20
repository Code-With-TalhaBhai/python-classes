## Heap
Heap is a complete binary tree which start filling from left towards right, in which all levels are filled, except possibly the last one.


### Heap Properties

***Heapify***: Heapify is a process used to transform a binary tree into a heap, a specialized tree-based data structure that satisfies the heap property. There are two types of heaps: max-heaps and min-heaps.

***Max Heap*** - In which parent node is greater than child node
***Min Heap*** - In which child node is greater than parent node

***Heapify Process***:Heapify can be done in two main ways:
    * Bottom-Up Approach(Heapify)
    * Top-Down Approach(Heap Insertion)

`If index starts from 1`
***Left-Child*** - 2 * current_index
***Right-Child*** - (2 * current_index) + 1
***Leaf-Nodes*** - `(n/2)+1 to n` (All are leaf-nodes)


`If index starts from 0`
***Left-Child*** - (2 * current_index) + 1
***Right-Child*** - (2 * current_index) + 2
***Leaf-Nodes*** - `(n/2) to n`(All are leaf-nodes)




## Time-Complexity
The worst-case time complexity of heapify depends on the algorithm used. The worst-case time complexity of bottom-up heapify is O(n), where n is the size of the heap. The worst-case time complexity of top-down heapify is O(n log n), where n is the size of the heap.



## Bottom-up VS Top-down HEAPIFY:
Bottom-up heapify starts at the lowest level of the heap and works its way up to the root, while top-down heapify starts at the root and works its way down to the lowest level of the heap. Bottom-up heapify has a time complexity of O(n), while top-down heapify has a time complexity of O(log n). Bottom-up heapify is typically faster for large heaps, while top-down heapify is faster for small heaps.



