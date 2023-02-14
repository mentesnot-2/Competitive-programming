class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        indx=0
        for i in range(len(arr)-1):
            if indx<=i:
                flag=arr[i+1]
                for j in range(i+2,len(arr)):
                    if arr[j]>flag:
                        flag=arr[j]
                        indx=j
                arr[i]=flag
            else:
                arr[i]=arr[indx]
        arr[-1]=-1
        return arr