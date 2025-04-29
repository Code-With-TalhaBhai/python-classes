

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



def reverse(head,prev):
    if not head:
        return prev

    next_node = head.next
    head.next = prev
    return reverse(next_node,head)


def reverse_node_in_k_group(head,cnt):

    temp_head = head
    k = 0
    while temp_head and k < cnt - 1:
        temp_head = temp_head.next
        k += 1


    if not temp_head:
        return head
    else:
        next_node = temp_head.next
        temp_head.next = None
        reverse(head,None)
        head.next = reverse_node_in_k_group(next_node,cnt)
    return temp_head
    



head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
print_list(head)
# new_head = reverse_node_in_k_group(head,3)
# print_list(new_head)
new_head = reverse_node_in_k_group(head,2)
print_list(new_head)
