class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '%d->%s' % (self.val, self.next)

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ans = None
        while head:
            newHead = head
            head = head.next
            newHead.next = ans
            ans = newHead
        return ans