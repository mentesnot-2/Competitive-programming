class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        val=int(sqrt(c))
        target=[i for i in range(1,val+2)]
        left=0
        right=len(target)-1
        while left<=right:
            if ((target[left])**2) + ((target[right])**2)>c:
                right-=1
            if ((target[left])**2) + ((target[right])**2)<c:
                left+=1
            else:
                return True
        return False