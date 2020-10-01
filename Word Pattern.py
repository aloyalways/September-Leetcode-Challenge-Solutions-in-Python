from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=list(map(str,s.split(" ")))
        if len(pattern)!=len(s):
            return False
        sDict=defaultdict(str)
        pDict=defaultdict(str)
        for i in range(len(s)):
            if sDict[s[i]]:
                if sDict[s[i]]!=pattern[i]:
                    return False
            else:
                if pDict[pattern[i]]:
                    return False
                sDict[s[i]]=pattern[i]
                pDict[pattern[i]]=s[i]
        return True
