def isPrefixAndSuffix(i,j):
    if i==j[0:len(i)] and i==j[-len(i):]:
        return True
    else:
        return False
    

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        c=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if isPrefixAndSuffix(words[i],words[j]):
                    c+=1
        return c

