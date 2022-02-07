from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return '%d->%s' % (self.val, self.next)

def deleteDuplicates(head: ListNode) -> ListNode:
    ln = head
    while ln and ln.next:
        if ln.next.val == ln.val:
            ln.next = ln.next.next
        else:
            ln = ln.next
    return head

print(deleteDuplicates(ListNode(1, ListNode(1, ListNode(2, None)))))
print(deleteDuplicates(ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, None)))))))
print(deleteDuplicates(ListNode(1, ListNode(2, ListNode(2, ListNode(2, ListNode(2, None)))))))