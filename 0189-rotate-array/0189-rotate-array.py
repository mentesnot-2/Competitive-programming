class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        r=len(nums)-1
        for i in range(k):
            last=nums.pop()
            nums.insert(0,last)
        return nums
        