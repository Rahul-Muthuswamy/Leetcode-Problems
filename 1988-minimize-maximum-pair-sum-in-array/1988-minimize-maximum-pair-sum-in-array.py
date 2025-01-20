class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxp=0
        for i in range(len(nums)//2):
            pair=nums[i]+nums[len(nums)-1-i]
            maxp=max(maxp,pair)
        return maxp