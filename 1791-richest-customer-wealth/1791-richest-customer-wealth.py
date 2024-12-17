class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        mw=0
        for i in accounts:
            tw=sum(i)
            mw=max(mw,tw)
        return mw