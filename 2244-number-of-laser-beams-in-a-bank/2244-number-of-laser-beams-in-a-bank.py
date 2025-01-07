class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        c = 0
        s = 0
        m = 0
        for i in bank:
            if s == 0:
                s = i.count('1')
            else:
                m = i.count('1')
                c += s*m
                if m>0:
                    s = m
        
        return c

        