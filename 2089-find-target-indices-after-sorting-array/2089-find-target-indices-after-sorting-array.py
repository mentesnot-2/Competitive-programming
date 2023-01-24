class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        targetI=[]
        for i in range(len(nums)):
            if nums[i]==target:
                targetI.append(i)
                
        return targetI