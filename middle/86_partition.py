class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return '%d -> %s' % (self.val, self.next)


def partition(head, x):
    left = ListNode()
    p = left
    right = ListNode()
    q = right
    while head:
        if head.val < x:
            p.next = head
            p = p.next
        else:
            q.next = head
            q = q.next
        head = head.next
    p.next = right.next
    q.next = None
    return left.next


print(partition(ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2)))))), 3))
print(partition(ListNode(2, ListNode(1)), 2))
