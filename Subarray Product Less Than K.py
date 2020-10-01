class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        product=1
        mini=0
        total=0
        subarrays=0
        
        for i in range(n):
            product*=nums[i]
            subarrays+=1
            
            while product>=k and mini<=i:
                product/=nums[mini]
                mini+=1
                subarrays-=1
            
            if product<k:
                total+=subarrays
        return total
