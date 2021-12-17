# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = head

        while curr:
            scur = dummy

            while scur.next and scur.next.val <= curr.val:
                scur = scur.next

            temp = scur.next
            scur.next = curr
            curr = curr.next
            scur.next.next = temp
        return dummy.next
