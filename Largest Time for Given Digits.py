from itertools import permutations
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        def time(hours,minutes):
            if int(hours)>=24 or int(minutes)>=60:
                return float('-inf')
            return int(hours)*60+int(minutes)
        maxTime=-1
        ans=""
        perm=list(permutations([0,1,2,3]))
        for i in perm:
            t=time(str(A[i[0]])+str(A[i[1]]),str(A[i[2]])+str(A[i[3]]))
            if t>maxTime:
                ans=""
                ans+=str(A[i[0]])+str(A[i[1]])+":"+str(A[i[2]])+str(A[i[3]])
                maxTime=t
        return ans
