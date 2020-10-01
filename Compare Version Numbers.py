class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i,j=0,0
        while i<len(version1) or j<len(version2):
            numi,numj=0,0
            while i<len(version1) and version1[i]!='.':
                numi=numi*10+int(version1[i])
                i+=1
            while j<len(version2) and version2[j]!='.':
                numj=numj*10+int(version2[j])
                j+=1
            if numi<numj:
                return -1
            elif numi>numj:
                return 1
            i+=1
            j+=1
        return 0
