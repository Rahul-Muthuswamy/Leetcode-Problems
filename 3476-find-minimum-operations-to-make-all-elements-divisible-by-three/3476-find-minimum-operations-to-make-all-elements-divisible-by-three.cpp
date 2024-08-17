class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        int r=0;
        for(auto i:nums){
            if(i%3!=0){
                r++;
            }
        }return r;
    }
};