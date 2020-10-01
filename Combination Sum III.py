from itertools import combinations
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums=[_ for _ in range(1,10)]
        ans=[]
        comb=combinations(nums,k)
        for i in comb:
            if sum(i)==n:
                ans.append(i)
        return ans
