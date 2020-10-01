from collections import defaultdict
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        start=defaultdict(list)
        end=defaultdict(list)
        endMax=-1
        for i in trips:
            start[i[1]].append(i[0])
            end[i[2]].append(i[0])
            endMax=max(endMax,i[2])
        for i in range(endMax+1):
            if capacity<0:
                return False
            if end[i]:
                for j in end[i]:
                    capacity+=j
            if start[i]:
                for j in start[i]:
                    capacity-=j
        return True
