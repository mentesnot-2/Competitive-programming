class Solution:
    def fib(self, n: int) -> int:
        if n==0: return 0
        elif n==1:return 1
      
        tb=[0,1]
        for i in range(2,n+1):
            tb.append(tb[i-1]+tb[i-2])
        return tb[n]