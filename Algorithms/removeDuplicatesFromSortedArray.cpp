class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        map<int, int> mp;
        for (int i=0 ; i<n ; i++){
            mp[nums[i]]++;
        }
        map<int, int>::iterator it = mp.begin();
        int j=0;
        for (auto map_it = mp.begin(); map_it != mp.end(); ++map_it) {
            nums[j] = map_it->first;
            j++;
        }

        return mp.size();
    }
};