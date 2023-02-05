class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num=Counter(nums)
        for i in num:
            if num[i]==1:
                return i
        