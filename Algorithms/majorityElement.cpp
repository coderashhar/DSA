class Solution {
public:
    vector<int> majorityElementTwo(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int, int> mp;
        for (int i=0 ; i<n ; i++){
            mp[nums[i]]++;
        }
        set<int> st;
        for (int i=0 ; i<n ; i++){
            if (mp[nums[i]] > n/3) st.insert(nums[i]);
        }
        vector<int> ans(st.begin(), st.end());
        return ans;
    }
};