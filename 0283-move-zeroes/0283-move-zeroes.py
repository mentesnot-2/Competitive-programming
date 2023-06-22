class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        notZero = 0
        
        for i in range(len(nums)):
            if nums[i] != 0 and nums[notZero] == 0:
                nums[i],nums[notZero] = nums[notZero],nums[i]
            if nums[notZero] != 0:
                notZero+=1
        return nums
        