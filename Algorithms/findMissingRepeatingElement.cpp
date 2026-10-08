class Solution {
public:
    vector<int> findMissingRepeatingNumbers(vector<int> nums) {
        map<int,int> mp;
        for (int i=0 ; i<nums.size() ; i++){
            mp[nums[i]]++;
        }
        int twice;
        int missing;
        for (int i=1 ; i<=nums.size() ; i++){
            if (mp.find(i) == mp.end()) missing = i;
            else if (mp[i] > 1) twice = i;
        }
        vector<int> ans = {twice, missing};
        return ans;
    }
};