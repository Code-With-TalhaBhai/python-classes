import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def traverse_list(head):
    while head:
        print(head.val,end=" -> ")
        head = head.next
    print()


l1 = ListNode(1)
l1.next = ListNode(4)
l1.next = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next = ListNode(4)

l3 = ListNode(2)
l3.next = ListNode(4)


sorted_lists = [l1,l2,l3]
heap_list = []


for i,single_list in enumerate(sorted_lists):
    if single_list:
        heapq.heappush(heap_list, (single_list.val, i,single_list)) # without i, gives error


ans_list = ListNode()
dummy = ans_list


while heap_list:
    val,i,node = heapq.heappop(heap_list)
    # dummy.next = ListNode(val)
    # dummy = dummy.next
    dummy.next = node
    dummy = node

    node = node.next
    if node:
        heapq.heappush(heap_list,(node.val,i,node))




traverse_list(ans_list.next)


