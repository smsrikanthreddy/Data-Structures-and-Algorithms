# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        def bst_tree(down, up, idx):
            if idx >= len(preorder):
                return (None, idx)
            if not down <= preorder[idx] <= up:
                return (None, idx)
            top = TreeNode(preorder[idx])
            top.left, idx = bst_tree(down, top.val, idx + 1)
            top.right, idx = bst_tree(top.val, up, idx)
            return top, idx

        return bst_tree(-float("inf"), float("inf"), 0)[0]
