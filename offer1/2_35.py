class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node'):
        if not head:
            return None
        node = head
        while node:
            newnode = Node(node.val)
            newnode.next = node.next
            node.next = newnode
            node = node.next.next
        node = head
        while node:
            newnode = node.next
            newnode.random = node.random.next if node.random is not None else None
            node = node.next.next
        node = head
        newhead = head.next
        while node:
            newnode = node.next
            node = newnode.next
            newnode.next = newnode.next.next if newnode.next is not None else None
        return newhead