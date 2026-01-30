# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        def cousins_trav(head, length, parent, xy):
            if not head:
                return None

            if head.val == xy:
                return parent, length

            return cousins_trav(head.left, length+1, head.val, xy) or cousins_trav(head.right, length+1, head.val, xy)

        lparent, llength = cousins_trav(root, 0, None, x)
        rparent, rlength = cousins_trav(root, 0, None, y)

        return lparent != rparent and llength == rlength
