class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        s = []
        r = []
        for i in nums:
            if i in s:
                r.append(i)
            else:
                s.append(i)
        return r
