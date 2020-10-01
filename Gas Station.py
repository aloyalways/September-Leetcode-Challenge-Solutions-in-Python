class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        tank,maxlen=0,0
        for i in range(n*2):
            tank+=(gas[i%n]-cost[i%n])
            if tank>=0:
                maxlen+=1
            else:
                maxlen=0
            tank=max(tank,0)
        if maxlen>=n:
            return n*2-maxlen
        return -1
