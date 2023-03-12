class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count=0
        prefix=[0]
        for i in range(len(nums)):
            prefix.append(prefix[-1]+nums[i])
        freq={}
        for i in prefix:
            if i%k in freq:
                count+=freq[i%k]
                freq[i%k]+=1
            elif i%k not in freq:
                freq[i%k]=0
                freq[i%k]+=1
        return count