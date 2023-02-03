class Solution:
    def countTriples(self, n: int) -> int:
        squre={}
        for i in range(1,n+1):
            squre[i]= i*i
        count=0
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if squre[i] + squre[j] in squre.values():
                    count+=2
        return count