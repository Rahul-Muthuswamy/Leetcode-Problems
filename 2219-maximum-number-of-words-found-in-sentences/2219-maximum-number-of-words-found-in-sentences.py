class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        c=[]
        for i in sentences:
            c.append(i.count(" "))
        return max(c)+1