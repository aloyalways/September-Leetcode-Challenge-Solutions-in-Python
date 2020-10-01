class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp=[[-1]*(n+1) for _ in range(n+1)]
        def helper(i,j):
            if i==n:
                return True
            if j==n:
                return False
            if dp[i][j]!=-1:
                return dp[i][j]
            if s[i:j+1] in wordDict:
                dp[i][j]=helper(i,j+1)|helper(j+1,j+1)
                return dp[i][j]
            else:
                dp[i][j]=helper(i,j+1)
                return dp[i][j]
        return helper(0,0)
