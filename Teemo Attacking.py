class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries)==0:
            return 0
        
        for i in range(len(timeSeries)):
            timeSeries[i]+=duration
        ans=duration
        for i in range(1,len(timeSeries)):
            if timeSeries[i]-timeSeries[i-1]<=duration:
                ans+=timeSeries[i]-timeSeries[i-1]
            else:
                ans+=duration
                
        return ans
