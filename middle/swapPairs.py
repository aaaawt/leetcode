from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return '%d -> %s' % (self.val, self.next)

def swapPairs(head: Optional[ListNode]):
    if not head:
        return None
    p = head
    new = ListNode()
    ans = new
    while p:
        ans.next = p.next
        ans.next.next = p
        p = p.next.next
    return ans


print(swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))))
print(swapPairs(ListNode(1, None)))
print(swapPairs(None))
