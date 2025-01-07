class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        c = 0
        for i in s:
            if i == '|':
                count += 1
            elif i == '*' and count%2==0:
                c += 1
        return c
        