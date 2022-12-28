class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dic={}
        lst=[]
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]]+=1
            else:
                dic[nums[i]]=1
        for i in dic:
            if dic[i]>1:
                lst.append(i)
        return lst
        