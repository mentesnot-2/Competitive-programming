class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = sorted(nums)
        
        check = {val:indx for val,indx in enumerate(num)}
        
        for i in check:
            if i != check[i]:
                return i
        return num[-1] + 1       
        