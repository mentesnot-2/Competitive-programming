class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        maxLen=0
        tank=0
        for i in range(2*len(gas)):
            tank+=(gas[i%len(gas)]-cost[i%len(gas)])
            if tank>=0:
                maxLen+=1
            else:
                maxLen=0
            tank=max(tank,0)
        if maxLen>=len(gas):
            return (len(gas)*2)-maxLen
        else:
            return -1