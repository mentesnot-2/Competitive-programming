class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        nums=0
        l=len(num)-1
        for i in range(len(num)):
            nums=nums+(10**(l-i) * num[i])
        nums+=k
        lst=[]
        nums=str(nums)
        for i in nums:
            lst.append(int(i))
            
        return lst