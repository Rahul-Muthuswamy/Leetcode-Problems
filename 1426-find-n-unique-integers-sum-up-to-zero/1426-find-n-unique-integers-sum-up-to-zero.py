class Solution:
    def sumZero(self, n: int) -> List[int]:
        a = []
        for i in range(1, n):
            a.append(i)
        a.append(-sum(a))
        return a
        a = [i for i in range(1,n)]
        a.append(-sum(a))
        return a