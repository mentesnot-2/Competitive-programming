class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        num=[]
        for i in nums:
            if i%2==0:
                num.append(i)
        for j in nums:
            if j%2!=0:
                num.append(j)
        return num