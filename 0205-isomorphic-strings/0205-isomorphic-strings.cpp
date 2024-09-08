#include <unordered_map>
#include <string>

class Solution {
public:
    bool isIsomorphic(string s,string t) {
        if (s.length() != t.length()) {
            return false;
        }
        unordered_map<char, char> charMappingMap;
        unordered_map<char, bool> mappedValues;
        for (int i = 0; i < s.length(); ++i) {
            char original = s[i];
            char replacement = t[i];
            if (charMappingMap.find(original) == charMappingMap.end()) {
                if (mappedValues.find(replacement) == mappedValues.end()) {
                    charMappingMap[original] = replacement;
                    mappedValues[replacement] = true;
                } else {
                    return false;
                }
            } else {
                char mappedCharacter = charMappingMap[original];
                if (mappedCharacter != replacement) {
                    return false;
                }
            }
        }
        return true;
    }
};
