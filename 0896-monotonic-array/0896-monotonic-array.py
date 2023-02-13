class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        temp=sorted(nums)
        if temp==nums or temp==nums[::-1]:
            return True
        
        else:
            return False  