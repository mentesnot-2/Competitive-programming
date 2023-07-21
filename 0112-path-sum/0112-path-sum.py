# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def recursive(node,cur_sum):
            if not node:
                return False
            
            cur_sum+=node.val
            if not node.left and not node.right:
                return cur_sum == targetSum
            return recursive(node.left,cur_sum) or recursive(node.right,cur_sum)
        
        return recursive(root,0)