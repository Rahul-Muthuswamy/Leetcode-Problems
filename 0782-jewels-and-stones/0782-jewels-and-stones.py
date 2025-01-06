class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        js=set(jewels)
        s=0
        for i in stones:
            if i in js:
                s+=1
        return s