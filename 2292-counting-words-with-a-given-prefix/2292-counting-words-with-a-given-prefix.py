class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        s=0
        for i in words:
            if i[0:len(pref)]==pref:
                s+=1
        return s