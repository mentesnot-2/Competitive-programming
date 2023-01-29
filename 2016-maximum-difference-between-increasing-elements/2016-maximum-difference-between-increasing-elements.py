class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        j=0
        res=-1
        while j<len(nums):
            for i in range(j+1,len(nums)):
                if nums[i]>nums[j]:
                    res=max(res,nums[i]-nums[j])
            j+=1
        return res