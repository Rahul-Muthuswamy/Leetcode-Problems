def z_function(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r and z[i - l] < r - i + 1:
            z[i] = z[i - l]
        else:
            z[i] = max(0, r - i + 1)
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    return z

class Solution:

    def beautifulSplits(self, nums: List[int]) -> int:

        size = len(nums)
        if size < 3:
            return 0

        ans = 0
        z1 = z_function(nums)

        for i in range(1, size):
            if z1[i] >= i:
                ans += size - 2 * i
                maxSize = 2 * i
            else:
                maxSize = size

            z2 = z_function(nums[i:])
            for j in range(i + 1, maxSize):
                if z2[j - i] >= j - i:
                    ans += 1
        return ans