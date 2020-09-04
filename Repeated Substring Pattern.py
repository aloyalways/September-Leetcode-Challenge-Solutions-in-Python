from collections import defaultdict
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ans=(s+s)[1:-1]
        return s in ans
