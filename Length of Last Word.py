class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length=0
        ans=[0]
        for i in s:
            if i==" ":
                if length!=0:
                    ans.append(length)
                length=0
            else:
                length+=1
        if length!=0:
            return length
        return ans[-1]
