class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        output=[]
        length=len(str(low))
        while length<=len(str(high)):
            i=1
            while i+length<=10:
                ans=""
                for j in range(i,i+length):
                    ans+=str(j)
                if int(ans)>=low and int(ans)<=high:
                    output.append(int(ans))
                i+=1
            length+=1
        return output
