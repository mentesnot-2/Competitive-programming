# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        queue=[root]
        while queue:
            val=len(queue)
            level=[]
            for i in range(val):
                top=queue.pop(0)
             
                if top:
                    level.append(top.val)
                  
                    queue.append(top.left)

                    queue.append(top.right)
                    
            if level:
                res.append(level)

        for i in range(1,len(res),2):
            res[i]=res[i][::-1]
        return res