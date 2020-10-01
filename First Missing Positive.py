class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=sorted(nums)
        ans=1
        for i in nums:
            if i==ans:
                ans+=1
        return ans
