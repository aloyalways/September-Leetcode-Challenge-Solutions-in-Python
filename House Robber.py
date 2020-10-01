class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(i,rob):
            if i>=len(nums):
                return 0
            if dp[i][rob]!=-1:
                return dp[i][rob]
            if rob:
                dp[i][rob]=max(nums[i]+helper(i+1,False),helper(i+1,rob))
                return dp[i][rob]
            else:
                dp[i][rob]=helper(i+1,True)
                return dp[i][rob]
        dp=[[-1]*2 for _ in range(len(nums))]
        return helper(0,True)
