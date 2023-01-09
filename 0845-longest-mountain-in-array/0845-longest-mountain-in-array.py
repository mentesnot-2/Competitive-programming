class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        longestMountain=0
        for i in range(1,len(arr)-1):
            if arr[i-1]<arr[i] and arr[i+1]<arr[i]:
                l=i-1
                r=i+1
                while l>0 and arr[l-1]<arr[l]:
                    l-=1
                while r<len(arr)-1 and arr[r+1]<arr[r]:
                    r+=1
                longestMountain=max(longestMountain,r-l+1)
        return longestMountain