class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n=len(A)
        
        def helper(x,y):
            num=0
            for r in range(n):
                for c in range(n):
                    if 0<=c+x<n and 0<=r+y<n and A[r+y][c+x]==1 and B[r][c]==1:
                        num+=1
            return num
        
        return max([helper(x,y) for x in range(-n,n) for y in range(-n,n)])
