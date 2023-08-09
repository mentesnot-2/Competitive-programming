# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        
        def pathSum(path,node):
            if not node:
                return 0
            path = path * 10 + node.val
            
            if not node.right and not node.left:

                return path
            return pathSum(path,node.left) + pathSum(path ,node.right)
        return pathSum(0,root)
