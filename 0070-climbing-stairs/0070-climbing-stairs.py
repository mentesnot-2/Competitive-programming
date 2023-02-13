class Solution:
    def climbStairs(self, n: int) -> int:
        tb=[1,2]
        if n==1: return 1
        elif n==2:return 2
        else:
            for i in range(2,n+1):
                tb.append(tb[i-1]+tb[i-2])
            return tb[n-1]