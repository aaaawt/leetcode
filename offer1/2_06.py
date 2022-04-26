class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '%d->%s' % (self.val, self.next)

class Solution:
    def reversePrint(self, head: ListNode):
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        ans.reverse()
        return ans

