class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = {}
        distinct = []
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for key, val in d.items():
            if val == 1:
                distinct.append(key)
        for i in range(len(distinct)):
            if i == k - 1:
                return distinct[i]
        return ""