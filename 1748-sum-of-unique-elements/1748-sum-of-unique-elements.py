class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        num=Counter(nums)
        uniqueSum=0
        for i in num:
            if num[i]==1:
                uniqueSum+=i
        return uniqueSum