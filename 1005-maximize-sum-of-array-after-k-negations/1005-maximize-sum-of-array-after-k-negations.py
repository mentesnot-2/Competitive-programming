class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        while k:
            nums.sort()
            nums[0]= (-1) *nums[0]
            k-=1
        tot=0
        for i in nums:
            tot+=i
        return tot