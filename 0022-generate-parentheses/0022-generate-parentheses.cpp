class Solution {
public:
    void dfs(int l, int r, string t, vector<string>& ans, int n) {
        if (l > n || r > n || l < r)
            return;
        if (l == n && r == n) {
            ans.push_back(t);
            return;
        }
        dfs(l + 1, r, t + '(', ans, n);
        dfs(l, r + 1, t + ')', ans, n);
    }

    vector<string> generateParenthesis(int n) {
        vector<string> ans;
        dfs(0, 0, "", ans, n);
        return ans;
    }
};
