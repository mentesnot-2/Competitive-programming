class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = [0] * len(nums)
        for i in range(len(nums)):
            stack[i] = -1
            for j in range(len(nums)):
                if (nums[(i + j) % len(nums)] > nums[i]):
                    stack[i] = nums[(i + j) % len(nums)]
                    break
        return stack