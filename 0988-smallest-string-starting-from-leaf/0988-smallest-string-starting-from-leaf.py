# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        path = ""
        stack = [(root,"")]
        
        while stack:
            node,s = stack.pop()
            
            if node:
                s = chr(node.val + 97) + s
                if not node.left and not node.right:
                    if s < path or path == "":
                        path = s
                else:
                    stack.append((node.left,s))
                    stack.append((node.right,s))
        return path