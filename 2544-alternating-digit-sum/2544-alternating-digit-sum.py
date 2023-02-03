class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n=str(n)
        tot=0
        for i in range(len(n)):
            if i%2==0:
                tot+=int(n[i])
            else:
                tot-=int(n[i])
        return tot