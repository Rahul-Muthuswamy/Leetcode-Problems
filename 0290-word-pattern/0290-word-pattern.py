class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        d = {}
        for i in range(len(words)):
            if pattern[i] not in d:
                if words[i] in d.values():
                    return False
                d[pattern[i]] = words[i]
            else:
                if d[pattern[i]] != words[i]:
                    return False
        return True
