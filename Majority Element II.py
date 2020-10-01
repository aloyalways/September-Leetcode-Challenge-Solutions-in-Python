from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majEle=len(nums)//3
        count=Counter(nums)
        ans=[]
        for i in count:
            if count[i]>majEle:
                ans.append(i)
        return ans
        
