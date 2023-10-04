class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ls = 0
        count = 0
        
        for i in nums:
            if i < target:
                ls+=1
            elif i == target:
                count+=1
        final = []
        
        for k in range(count):
            final.append(k + ls)
        return final