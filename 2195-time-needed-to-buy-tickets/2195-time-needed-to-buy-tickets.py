class Solution:
    def timeRequiredToBuy(self, t: List[int], k: int) -> int:
        n=len(t)
        x=t[k]
        time=0
        for i, y in enumerate(t):
            buy=x
            if i>k: buy=x-1
            time+=min(buy, y)
        return time
        