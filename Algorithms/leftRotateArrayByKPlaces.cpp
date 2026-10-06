class Solution {
public:
    void rotateArray(vector<int>& nums, int k) {
        int n = k;
        if (k > nums.size()) n = k % nums.size();
        reverse(nums.begin(), nums.end());
        reverse(nums.begin(), nums.end()-n);
        reverse(nums.end()-n, nums.end());
    }
};