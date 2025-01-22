class Solution {
    string s;
public:
    string expand(int l, int r) {
        while(l >= 0 and r < s.size() and s[l] == s[r]) {
            l--;    r++;
        }
        return s.substr(l + 1, r - l - 1);
    }
    string longestPalindrome(string tmp) {
        s = tmp;
        string odd, even, ans = "";
        for(int i = 0; i < s.size(); i++) {
            odd = expand(i, i);
            if(odd.size() > ans.size()) ans = odd;
            even = expand(i, i + 1);
            if(even.size() > ans.size()) ans = even;
        }
        return ans;
    }
};