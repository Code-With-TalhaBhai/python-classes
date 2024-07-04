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



