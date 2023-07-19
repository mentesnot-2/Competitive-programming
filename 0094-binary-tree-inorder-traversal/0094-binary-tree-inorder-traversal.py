# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        val = []
        if not root:
            return []
        else:
            val+=self.inorderTraversal(root.left) 
            val.append(root.val) 
            val+=self.inorderTraversal(root.right)
        return val
             
        