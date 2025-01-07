class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s=""
        r=""
        for j in word1:
            r+=j
        for i in word2:
            s+=i
        if s==r:
            return True
        else:

            return False
            