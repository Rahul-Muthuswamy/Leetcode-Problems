class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        para = {"(": ")", "{": "}", "[": "]"}
        for p in s:
            if p in para:
                stack.append(p)
            elif stack and para[stack[-1]] == p:
                stack.pop()
            else:
                return False
        return not stack
