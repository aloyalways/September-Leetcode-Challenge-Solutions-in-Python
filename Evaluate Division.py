from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        hashSet=defaultdict(list)
        for i in range(len(equations)):
            hashSet[equations[i][0]].append((equations[i][1],values[i]))
            hashSet[equations[i][1]].append((equations[i][0],1/values[i]))
        
        def dfs(node,deno,ans):
            visited.append(node)
            if node==deno:
                return ans
            b=-1.0
            for neighbour in hashSet[node]:
                if neighbour[0] not in visited:
                    a=dfs(neighbour[0],deno,ans*neighbour[1])
                    b=max(b,a)
            return b
        
        ans=[]
        for i in queries:
            visited=[]
            if not hashSet[i[0]] or not hashSet[i[1]]:
                ans.append(-1.0)
                continue
            ans.append(dfs(i[0],i[1],1.0))
        return ans
            
