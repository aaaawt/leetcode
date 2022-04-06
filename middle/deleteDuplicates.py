class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return '%d -> %s' % (self.val, self.next)


def deleteDuplicates(head):
    if not head:
        return
    ans = ListNode()
    node = ans
    val = 301
    while head.next:
        if head.val != val and head.val != head.next.val:
            node.next = head
            node = node.next
        elif head.val != val and head.next.val == head.val:
            val = head.val
        head = head.next
    if head.val != val:
        node.next = head
    else:
        node.next = None
    return ans.next


print(deleteDuplicates(ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))))
print(deleteDuplicates(ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3)))))))
print(deleteDuplicates(ListNode(1, ListNode(2, ListNode(2)))))
