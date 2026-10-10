class Solution{
public:
    int longestSubarray(vector<int> &nums, int k){
        int n = nums.size();
        unordered_map<int, int> mp;
        mp[0] = -1;
        int sum = 0;
        int maxlen = 0;
        for (int i=0 ; i<n ; i++){
            sum += nums[i];
            if (mp.find(sum - k) != mp.end()){
                maxlen = max(maxlen, i - mp[sum - k]);
            }
            if (mp.find(sum) == mp.end()) mp[sum] = i;
        }
        return maxlen;
    }
};
