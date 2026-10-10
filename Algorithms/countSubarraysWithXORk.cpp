class Solution{
public:
    int subarraysWithXorK(vector<int> &nums, int k) {
        int n = nums.size();
        unordered_map<int, int> mp;
        int prefix = 0;
        int count = 0;
        mp[0] = 1;
        for (int i=0 ; i<n ; i++){
            prefix ^= nums[i];
            if (mp.find(prefix^k) != mp.end()){
                count += mp[prefix ^ k];
            }
            mp[prefix]++;
        }
        return count;
    }
};

