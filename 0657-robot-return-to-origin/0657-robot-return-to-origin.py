class Solution:
    def judgeCircle(self, moves: str) -> bool:
        y=0
        z=0
        for i in moves:
            if i=='U':
                y+=1
            elif i=="D":
                y-=1
            elif i=="R":
                z+=1
            elif i=="L":
                z-=1
        if y==0 and z==0:
            return True
        else:
            return False

            
