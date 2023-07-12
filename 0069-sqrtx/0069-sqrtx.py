import math
class Solution:

    def mySqrt(self, x: int) -> int:
        left,right = 1,x
        val = 0
        while left <= right:
            mid = left + (right - left)//2
            
            if (mid * mid) < x:
                left = mid + 1
            elif (mid * mid) > x:
                right = mid - 1
                
            else:
                return mid 
            val = mid
        return val - 1 if val * val > x else val