class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        min_unfairnes = float("inf")
        dist = [0] * k
        def backtrack(i):
            nonlocal min_unfairnes,dist
            if i == len(cookies):
                min_unfairnes = min(min_unfairnes,max(dist))
                return
            if min_unfairnes <= max(dist): return
            for j in range(k):
                dist[j]+=cookies[i]
                backtrack(i + 1)
                dist[j]-=cookies[i]
        
        
        backtrack(0)
        return min_unfairnes