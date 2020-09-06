class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last={char:i for i,char in enumerate(S)}
        output,maxi,size=[],-1,1
        
        for i,char in enumerate(S):
            maxi=max(maxi,last[char])
            if i==maxi:
                output.append(size)
                size=1
            else:
                size+=1
        return output
