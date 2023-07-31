class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left,right = 0,len(arr) - 1
        while left <= right:
            mid = left + (right - left) //2
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid] < arr[mid + 1]  and arr[mid] > arr[mid - 1]:
                left = mid
            elif arr[mid] < arr[mid - 1]  and arr[mid] > arr[mid + 1]:
                right = mid