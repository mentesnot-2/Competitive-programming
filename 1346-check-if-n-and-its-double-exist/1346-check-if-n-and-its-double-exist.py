class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dic={}
        for i in arr:
            dic[i]=i*2
        for i in dic:
            if i==0 and arr.count(0)>1:
                return True
            elif dic[i] in arr and arr.index(i)!=arr.index(dic[i]):
                return True
        return False