class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return '%d -> %s'%(self.val, self.next)

def addTwoNumbers(l1: ListNode, l2: ListNode):
    k = 0
    res = ListNode()
    head = res
    while l1 and l2:
        res.next = ListNode()
        res = res.next
        res.val = (l1.val + l2.val + k) % 10
        k = (l1.val + l2.val + k) // 10
        l1, l2 = l1.next, l2.next
    if not l1 and not l2 and k != 0:
        res.next = ListNode()
        res = res.next
        res.val = k
    if not l1 and l2:
        while l2:
            res.next = ListNode()
            res = res.next
            res.val = (l2.val + k) % 10
            k = (l2.val + k) // 10
            l2 = l2.next
        if k != 0:
            res.next = ListNode()
            res = res.next
            res.val = k
    if not l2 and l1:
        while l1:
            res.next = ListNode()
            res = res.next
            res.val = (l1.val + k) % 10
            k = (l1.val + k) // 10
            l1 = l1.next
        if k != 0:
            res.next = ListNode()
            res = res.next
            res.val = k
    return head.next

print(addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4)))))
print(addTwoNumbers(ListNode(0), ListNode(0)))
print(addTwoNumbers(ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))),
                    ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))