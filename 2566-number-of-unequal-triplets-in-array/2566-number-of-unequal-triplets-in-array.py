class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        s=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i<j and j<k and k<len(nums):
                        if nums[i]!=nums[j] and nums[i]!=nums[k]and nums[j]!=nums[k]:
                            s+=1
        return s