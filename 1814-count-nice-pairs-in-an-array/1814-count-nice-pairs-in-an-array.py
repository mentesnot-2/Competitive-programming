class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(num,count = 0):
            while num != 0:
                rem = num % 10
                count = count * 10 + rem
                num = num // 10
            return count
        for i in range(len(nums)):
            nums[i] = rev(nums[i]) - nums[i]
            
        dct = {}
        total = 0
        
        for i in nums:
            if i in dct:
                total+=dct[i]
            elif i not in dct:
                dct[i] = 0
            dct[i]+=1
        return total % (10**9 + 7)