# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        l,r=0,0
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            l=root.left.val
        else:
            l=self.sumOfLeftLeaves(root.left)
        r=self.sumOfLeftLeaves(root.right)
        return l+r