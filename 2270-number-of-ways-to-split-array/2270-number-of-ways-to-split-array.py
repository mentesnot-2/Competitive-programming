class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total=0
        for i in nums:
            total+=i
        validSplit=0
        count=0
        for j in range(len(nums)-1):
            validSplit+=nums[j]
            if validSplit>=total-validSplit:
                count+=1
        return count