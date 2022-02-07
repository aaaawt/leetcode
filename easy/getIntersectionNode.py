class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

def getIntersectionNode(headA: ListNode, headB: ListNode):
    tempA = headA
    tempB = headB
    while tempA != tempB:
        if tempA is not None:
            tempA = tempA.next
        else:
            tempA = headB
        if tempB is not None:
            tempB = tempB.next
        else:
            tempB = headA
    return tempA

    # while headA:
    #     tempB = headB
    #     while tempB:
    #         if headA == tempB:
    #             return headA.val
    #         tempB = tempB.next
    #     headA = headA.next
    # return None

inter1 = ListNode(8, ListNode(4, ListNode(5)))
print(getIntersectionNode(ListNode(4, ListNode(1, inter1)), ListNode(5, ListNode(6, ListNode(1, inter1)))))
inter2 = ListNode(2, ListNode(4))
print(getIntersectionNode(ListNode(1, ListNode(9, ListNode(1, inter2))), ListNode(3, inter2)))
print(getIntersectionNode(ListNode(2, ListNode(6, ListNode(4))), ListNode(1, ListNode(5))))