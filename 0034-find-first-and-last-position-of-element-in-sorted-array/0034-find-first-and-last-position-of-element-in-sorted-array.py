class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def helperFirst(low,high,nums,target):
            if high >= low:
                mid = low + ( high - low )//2
                if ((mid == 0 or target > nums[ mid -1]) and nums[mid] == target):
                    return mid
                elif target > nums[mid]:
                    return helperFirst((mid+1),high,nums,target)
                else:
                    return helperFirst(low,(mid-1),nums,target)
            return -1
        
        def helperLast(low,high,nums,target):
            if (high >= low):
                mid = low + (high -low)//2
                
                if ((mid == len(nums)-1 or target < nums[mid+1]) and nums[mid] == target):
                    return mid
                elif target < nums[mid]:
                    return helperLast(low,(mid -1),nums,target)
                else:
                    return helperLast((mid+1),high,nums,target)
            return -1
        return [helperFirst(0,len(nums)-1,nums,target),helperLast(0,len(nums)-1,nums,target)]