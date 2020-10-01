from collections import defaultdict
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letter=defaultdict(lambda : 0)
        for i in s:
            letter[i]+=1
        for i in t:
            if letter[i]==0:
                return i
            letter[i]-=1
