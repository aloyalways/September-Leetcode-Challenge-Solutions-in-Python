class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if len(nums)<=1 or k==0:
            return False
        if t==0 and len(nums)==len(set(nums)):
            return False
        for idx,val in enumerate(nums):
            for j in range(idx+1,min(idx+k+1,len(nums))):
                if abs(val-nums[j])<=t:
                    return True
        return False
            
