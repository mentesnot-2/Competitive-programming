class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        if original not in nums:
            return original
        else:
            return self.findFinalValue(nums,2 * original)