class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l=0
        shuffled=[]
        r=len(nums)//2
        while l<len(nums)//2 and r<len(nums):
            shuffled.append(nums[l])
            shuffled.append(nums[r])
            l+=1
            r+=1
        return shuffled