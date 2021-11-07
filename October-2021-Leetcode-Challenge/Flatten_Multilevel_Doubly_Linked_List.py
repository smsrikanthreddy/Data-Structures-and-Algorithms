"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    ## TC - O(n)
    ## SC - O(1)
    def flatten(self, head: 'Node') -> 'Node':
        curr = head
        while curr:
            if curr.child is None:
                curr = curr.next
            else:
                tail = curr.child
                while tail.next:
                    tail = tail.next
                tail.next = curr.next
                if curr.next:
                    curr.next.prev = tail
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
        return head

# implement using stack
