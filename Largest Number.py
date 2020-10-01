class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def largest(a,b):
            if a+b>=b+a:
                return False
            else:
                return True
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if largest(str(nums[i]),str(nums[j])):
                    nums[i],nums[j]=nums[j],nums[i]
        
        return str(int(''.join(map(str,nums))))
