class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        startR,startC,endR,endC,empty=0,0,0,0,0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    startR,startC=i,j
                if grid[i][j]==2:
                    endR,endC=i,j
                if grid[i][j]==0:
                    empty+=1
         
        self.output=0
        visited=set()
        def dfs(r,c,visited,walk):
            if r==endR and c==endC:
                if walk==empty+1:
                    self.output+=1
                return
            if 0<=r<m and 0<=c<n and grid[r][c]!=-1 and (r,c) not in visited:
                visited.add((r,c))
                for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
                    dfs(r+i,c+j,visited,walk+1)
                visited.remove((r,c))
        dfs(startR,startC,visited,0)
        return self.output
