class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        A = nums
        N = len(A)
        P = [0]
        
        for x in A:
            P.append(P[-1] + x)
            
        ans = N + 1
        monoq = deque()
        for y,py in enumerate(P):
            while monoq and py <= P[monoq[-1]]:
                monoq.pop()
            while monoq and py - P[monoq[0]] >= k:
                ans = min(ans,y - monoq.popleft())
            monoq.append(y)
        return ans if ans < N + 1 else -1
        