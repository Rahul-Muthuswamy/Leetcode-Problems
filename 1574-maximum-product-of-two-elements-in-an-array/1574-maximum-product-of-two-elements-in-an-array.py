
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        arr = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                arr.append((nums[i] - 1) * (nums[j] - 1))  
        return max(arr) 
