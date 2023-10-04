# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(lambda: set())
        
        queue = [root]
        while queue:
            node = queue.pop(0)
            
            for ch in [node.left,node.right]:
                if ch:
                    queue.append(ch)
                    graph[node.val].add(ch.val)
                    graph[ch.val].add(node.val)
        queue = [(start,-1,0)]
        ans = 0
        while queue:
            node,prev,val = queue.pop(0)
            ans = max(ans,val)
            
            for i in graph[node]:
                if i != prev:
                    queue.append((i,node,val + 1))
        return ans