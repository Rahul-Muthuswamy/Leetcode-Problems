class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        m = [min(n[0], n[1])**2 for n in rectangles]
        return m.count(max(m))