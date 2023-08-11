import heapq
class Solution:
    def largestInteger(self, num: int) -> int:
        evenList = []
        oddList = []
        nums =[int(x) for x in str(num)]
        
        for i in nums:
            if i % 2 == 0:
                evenList.append(i)
            else:
                oddList.append(i)
                
        even = [-x for x in evenList]
        odd = [-x for x in oddList]
        
        heapq.heapify(even)
        heapq.heapify(odd)
        
        res = []
        
        for val in nums:
            if val in evenList:
                res+=[-heapq.heappop(even)]
            if val in oddList:
                res+=[-heapq.heappop(odd)]
                
        result =[str(x) for x in res] 
        
        return int(''.join(result))