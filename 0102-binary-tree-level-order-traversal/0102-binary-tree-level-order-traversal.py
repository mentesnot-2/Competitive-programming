# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level = []
        queue = [root]
        
        while queue:
            order = []
            val = len(queue)
            for i in range(val):
                cur = queue.pop(0)
                if cur:
                    order.append(cur.val)
                    
                    queue.append(cur.left)

                    queue.append(cur.right)
            if order:
                level.append(order)
        return level