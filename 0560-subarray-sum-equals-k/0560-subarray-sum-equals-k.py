class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum=[0]
        for i in range(len(nums)):
            prefixSum.append(prefixSum[-1]+nums[i])
        freq={}
        count=0
        for num in prefixSum:
            if (num-k) in freq:
                count+=freq[num-k]
            if num not in freq:
                freq[num]=0
            freq[num]+=1
        return count