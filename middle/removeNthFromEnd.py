class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return '%d -> %s' % (self.val, self.next)

def removeNthFromEnd(head: ListNode, n):
    p = head
    if p.next is None:
        return None
    i = 0
    while i < n:
        if p.next is None:
            p = head
        else:
            p = p.next
        i += 1
    q = head
    while p.next and p != q:
        q = q.next
        p = p.next
    if n == 1:
        q.next = None
    elif p == q:
        head = head.next
    else:
        q.next = q.next.next
    return head


print(removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))), 2))
print(removeNthFromEnd(ListNode(1, None), 1))
print(removeNthFromEnd(ListNode(1, ListNode(2, None)), 1))
print(removeNthFromEnd(ListNode(1, ListNode(2, None)), 2))
print(removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4,
                    ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10, None)))))))))), 7))

