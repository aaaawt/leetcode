from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return '%d->%s' % (self.val, self.next)

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    ln = ListNode(0, None)
    head = ln
    while list1 or list2:
        if not list1 or list2 and list2.val <= list1.val:
            ln.next, list2 = list2, list2.next
        else:
            ln.next, list1 = list1, list1.next
        ln = ln.next
    return head.next

print(mergeTwoLists(ListNode(1, ListNode(2, ListNode(4, None))),
                    ListNode(1, ListNode(3, ListNode(4, None)))))
print(mergeTwoLists(None, None))
print(mergeTwoLists(None, ListNode(0, None)))