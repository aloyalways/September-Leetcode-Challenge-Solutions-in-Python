class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans, cur_max, cur_min=-sys.maxsize, 0, 0
        for num in nums:
            if num>0: 
                cur_max,cur_min=max(num,num*cur_max), min(num, num*cur_min)
            else: 
                cur_max, cur_min=max(num, num*cur_min), min(num, num*cur_max)  
            ans = max(ans, cur_max)    
        if ans:
            return ans 
        else:
            return max(nums)
