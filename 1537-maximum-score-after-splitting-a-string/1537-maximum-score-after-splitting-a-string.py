class Solution:
    def maxScore(self, s: str) -> int:
        m, o, z = 0, 0, 0
        n = len(s)
        for i in range(n):
            if s[i] == '1':
                o += 1
        for i in range(n - 1):
            if s[i] == '0':
                z += 1
            else:
                o -= 1
            m = max(m, z + o)
        return m