class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size();
        int pivotidx = -1;
        for (int i=n-1 ; i>0 ; i--){
            if (nums[i-1] < nums[i]){
                pivotidx = i;
                break;
            } 
        }
        if (pivotidx == -1) reverse(nums.begin(), nums.end());
        else {
            for (int i=n-1 ; i>pivotidx ; i--){
                if (nums[i] > nums[pivotidx]){
                    swap(nums[pivotidx], nums[i]);
                    break;
                } 
            }
            reverse(nums.begin()+pivotidx+1, nums.end());
        } 
    }
};