class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr1=arr.copy()
        arr1.sort()
        dicS={}
        l=1
        for i in range(len(arr1)):
            if arr1[i] not in dicS:
                dicS[arr1[i]]=l
                l+=1
        for j in range(len(arr)):
            arr[j]=dicS[arr[j]]
        return arr
    