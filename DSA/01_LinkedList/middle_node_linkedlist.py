

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def linkedlist_middle(head):
    slow = head
    fast = head.next

    while fast:
        slow = slow.next
        fast = fast.next
        if not fast:
            break
        fast = fast.next
    return slow.val





head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6) #even number

# print(linkedlist_middle(head)) # odd number of node 3
print(linkedlist_middle(head)) # even number of node 4