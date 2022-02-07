from typing import Optional


class ListNode:
    def __init__(self, x: int, next: Optional['ListNode'] = None):
        self.val = x
        self.next = next

def hasCycle(head: Optional[ListNode]):
    if not head or not head.next:
        return False
    fast = head.next
    slow = head
    while fast != slow:
        if not fast or not fast.next:
            return False
        fast = fast.next.next
        slow = slow.next
    return True


loop1 = ListNode(2)
loop1.next = ListNode(0, ListNode(4, loop1))
print(hasCycle(ListNode(3, loop1)))
loop2 = ListNode(1)
loop2.next = ListNode(2, loop2)
print(hasCycle(loop2))
print(hasCycle(ListNode(1)))