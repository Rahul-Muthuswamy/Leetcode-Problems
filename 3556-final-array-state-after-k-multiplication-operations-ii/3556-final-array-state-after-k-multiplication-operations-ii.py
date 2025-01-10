class Solution:
    def getFinalState(self, A: List[int], K: int, M: int) -> List[int]:
        if M == 1: return A
        MOD = 10 ** 9 + 7
        N = len(A)
        
        B = [[x, i] for i,x in enumerate(A)]
        heapify(B)
        count = [0] * N

        while K and B[0][0] <= 1e9:
            K -= 1
            b, i = heappop(B)
            count[i] += 1
            heappush(B, [b * M, i])
        
        q, r = divmod(K, N)
        B.sort()
        for ix, (b, i) in enumerate(B):
            count[i] += q + (ix < r)
        
        for i, c in enumerate(count):
            A[i] *= pow(M, c, MOD)
            A[i] %= MOD
        
        return A