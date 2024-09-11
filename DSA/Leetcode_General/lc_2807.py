# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertGreatestCommonDivisors(head):

    temp = head
    temp_next = temp.next

    while temp_next is not None:

        if temp_next is not None:
            a = temp.val
            b = temp_next.val
            # for i in range(1,min(a,b)+1):
            #     if a % i == 0 and b % i == 0:
            #         gcd = i
            # temp.next = ListNode(gcd)
            while b:
                    a, b = b, a % b
            temp.next = ListNode(a)
            temp = temp.next
            temp.next = temp_next

        temp = temp.next
        temp_next = temp.next

    return head


def print_list(head):
    temp = head
    while temp:
        print(temp.val,end=" ")
        temp = temp.next
    print()


head = ListNode(18)
head.next = ListNode(6)
head.next.next = ListNode(10)
head.next.next.next = ListNode(3)

print_list(head)
print_list(insertGreatestCommonDivisors(head))
        