class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        windowSum=0
        start=0
        count=0
        for i in range(len(arr)):
            windowSum+=arr[i]
            if (i-start+1)==k:
                if (windowSum/k)>=threshold:
                    count+=1
                windowSum-=arr[start]
                start+=1
        return count