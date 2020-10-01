class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x,y=0,0
        point="up"
        for _ in range(4):
            for i in instructions:
                if i=="G":
                    if point=="up":
                        y+=1
                    elif point=="down":
                        y-=1
                    elif point=="left":
                        x-=1
                    else:
                        x+=1
                elif i=="L":
                    if point=="up":
                        point="left"
                    elif point=="down":
                        point="right"
                    elif point=="left":
                        point="down"
                    else:
                        point="up"
                elif i=="R":
                    if point=="up":
                        point="right"
                    elif point=="down":
                        point="left"
                    elif point=="left":
                        point="up"
                    else:
                        point="down"
            if x==0 and y==0:
                return True
        return False
