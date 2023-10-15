class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        a,b = 0,len(plants) - 1
        canA,canB = capacityA,capacityB
        refill = 0
        while a <= b:
            if a == b:
                if max(canA,canB) < plants[b]:
                    refill+=1
                return refill
            elif canA < plants[a]:
                refill+=1
                canA = capacityA
            if canB < plants[b]:
                refill+=1
                canB = capacityB
            canA-=plants[a]
            canB-=plants[b]
            a+=1
            b-=1
        return refill
        


                    
        