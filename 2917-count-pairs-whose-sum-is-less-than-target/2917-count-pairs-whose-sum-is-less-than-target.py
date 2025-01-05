class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        return sum(
            a + b < target
            for a, b in combinations(nums, 2)
        )