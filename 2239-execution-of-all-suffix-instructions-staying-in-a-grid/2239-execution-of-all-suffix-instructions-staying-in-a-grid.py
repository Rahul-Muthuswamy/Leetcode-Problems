class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        row,col,res=startPos[0],startPos[1],[]
        for i in range(len(s)):
            startPos[0],startPos[1],arr,count=row,col,s[i:],0
            for j in arr:
                if j=="R":
                    if startPos[1]+1==n:break
                    else:
                        startPos[1]+=1
                        count+=1
                elif j=="L":
                    if startPos[1]-1==-1:break
                    else:
                        startPos[1]-=1
                        count+=1
                elif j=="U":
                    if startPos[0]-1==-1:break
                    else:
                        startPos[0]-=1
                        count+=1
                elif j=="D":
                    if startPos[0]+1==n:break
                    else:
                        startPos[0]+=1
                        count+=1
            res.append(count)
        return res