from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return '%d -> %s' % (self.val, self.next)

def rotateRight(head:Optional[ListNode], k):
    if not head:
        return None
    if k == 0:
        return head
    count = 1
    ln1 = head
    while ln1.next:
        ln1 = ln1.next
        count += 1
    if count == 1 or k % count == 0:
        return head
    n = count - k % count
    ln2 = head
    i = 0
    while i < n - 1:
        ln2 = ln2.next
        i += 1

    res = ln2.next
    ln1.next = head
    ln2.next = None
    return res

print(rotateRight(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))), 2))
print(rotateRight(ListNode(1, ListNode(2)), 2))
