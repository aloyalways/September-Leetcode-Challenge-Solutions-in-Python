from collections import defaultdict
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n=len(secret)
        secret=list(secret)
        guess=list(guess)
        a,b=0,0
        index=[]
        for i in range(n):
            if secret[i]==guess[i]:
                a+=1
                index.append(i)
        t=0
        for i in index:
            secret.pop(i-t)
            guess.pop(i-t)
            t+=1
        for i in range(len(guess)):
            if guess[i] in secret:
                b+=1
                secret.remove(guess[i])
        return "{}A{}B".format(a,b)
                
