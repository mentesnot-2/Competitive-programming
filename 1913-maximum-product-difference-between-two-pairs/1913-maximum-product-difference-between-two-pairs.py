class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        first=0
        second=0
        for num in nums:
            if num>first:
                second=first
                first=num
            elif num>second:
                second=num
        pro=first*second
        first=float("inf")
        second=float("inf")
        for num in nums:
            if num<first:
                second=first
                first=num
            elif num<second:
                second=num
        pro1=first*second
        return pro-pro1