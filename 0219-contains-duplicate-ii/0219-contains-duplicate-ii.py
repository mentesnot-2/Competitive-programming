class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        count={}
        for i ,j in enumerate(nums):
            if j in count and abs(i-count[j])<=k:
                return True
            else:
                count[j]=i
        return False
        