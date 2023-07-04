class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [0] * len(nums)
        for i in range(2 * len(nums) -1,-1,-1):
            while (stack and nums[stack[-1]] <= nums[ i% len(nums) ]):
                stack.pop()
            res[ i % len(nums) ] = -1 if stack == [] else nums[stack[-1]]
            stack.append((i % len(nums)))
        return res