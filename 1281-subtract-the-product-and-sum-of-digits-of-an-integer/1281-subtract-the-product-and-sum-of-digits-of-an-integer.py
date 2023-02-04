class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        tot=0
        prod=1
        while (n!=0):
            m=n%10
            tot+=m
            prod=prod*m
            n=n//10
        return prod-tot