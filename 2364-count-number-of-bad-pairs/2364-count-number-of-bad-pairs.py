class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        c = Counter()
        total = 0
        matched = 0
        
        for i,k in enumerate(nums):
            matched+=c[i - k]
            total+=i
            c[i - k]+=1
        
        return total - matched