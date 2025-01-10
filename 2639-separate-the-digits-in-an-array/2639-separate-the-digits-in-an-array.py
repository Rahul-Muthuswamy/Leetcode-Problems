class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        s=[]
        for i in nums:
            if len(str(i))==1:
                s.append(i)
            else:
                for j in str(i):
                    s.append(int(j))
        return s