class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        v = nums
        s = deque()
        n = len(v)
        
        for j in range(n - 1, -1, -1):
            cur = v[j]
            steps = 0
            
            while s:
                top = s[-1]
                if top[0] >= cur:
                    break
                
                steps = max(steps + 1, top[1])
                s.pop()
            
            s.append((cur, steps))
        
        ans = 0
        while s:
            ans = max(ans, s[-1][1])
            s.pop()
        
        return ans
