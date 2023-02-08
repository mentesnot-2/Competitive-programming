class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        index = 0
        for i in range(len(arr) - 1):
            
            if index <= i:
                flag = arr[i + 1]

                for j in range(i+1,len(arr)):
                    if arr[j]>flag:
                        flag=arr[j]
                        index = j
                arr[i] = flag
            else:
                arr[i] = arr[index]
        arr[-1]=-1
        return arr
        