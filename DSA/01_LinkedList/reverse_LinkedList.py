



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(node):
    curr_node = node
    while curr_node is not None:
        print(curr_node.val,end=" ")
        curr_node = curr_node.next
    print()


def reverse_list_iterative(head):
    if head is None:
            return None

    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node 
    return prev 





def reverse_list_recurrsive(head,prev=None):
    if head is None:
        # return prev
        return None
    
    next_node = head.next
    head.next = prev
    prev = head
    head = next_node
    return reverse_list_recurrsive(head,prev)

    # reverse_list_recurrsive(head.next,head)
    # head.next = prev
    # return head



    



head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)


print_list(head)
# new_head1 = reverse_list_iterative(head)
# print_list(new_head1)
new_head2 = reverse_list_recurrsive(head)
print_list(new_head2)
