class Solution:
    def countPoints(self, rings: str) -> int:
        r,g,b = [],[],[]
        for i in range(len(rings)):
            if rings[i] == "R": r.append(rings[i+1])
            if rings[i] == "G": g.append(rings[i+1])
            if rings[i] == "B": b.append(rings[i+1])
        return len((set(r).intersection(set(g))).intersection(set(b)))