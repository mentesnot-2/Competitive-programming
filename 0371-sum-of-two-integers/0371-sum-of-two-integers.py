class Solution:
    def getSum(self, a: int, b: int) -> int:
        if b==0:
            return a
        elif b>0:
            for i in range(1,b+1):
                a=a+1
        else:
            for j in range(1,(-1*b)+1):
                a=a-1
        return a