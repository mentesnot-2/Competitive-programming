class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        tot=sum(nums)
        res=0
        for i in nums:
            if i>=0 and i<=9:
                res+=i
            else:
                while (i!=0):
                    res+=i%10
                    i=i//10
        return abs(tot-res)
        