class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rule =["type", "color", "name"]
        rule_index= rule.index(ruleKey)
        count=0
        for item in items:
            if item[rule_index] == ruleValue:
                count += 1
        return count