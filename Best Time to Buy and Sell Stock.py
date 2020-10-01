class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        dp=[[float('-inf')]*2 for _ in range(len(prices)+1)]
        def solve(i,buy):
            if i==len(prices)-1:
                if buy:
                    return 0
                else:
                    return prices[i]
                
            if dp[i][buy]!=float('-inf'):
                return dp[i][buy]
            
            if buy:
                dp[i][buy]=max(solve(i+1,False)-prices[i],solve(i+1,True))
                return dp[i][buy]
            else:
                dp[i][buy]=max(prices[i],solve(i+1,False))
                return dp[i][buy]
        
        return solve(0,True)
                
