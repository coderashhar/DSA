class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int count = 0;
        int n = nums.size();
        vector<int> arr(n,0);
        int idx=0;
        for (int i=0 ; i<n ; i++){
            if (nums[i] != 0){
                count++;
                arr[idx] = nums[i];
                idx++;
            }
        }
        for (int i=0 ; i<n ; i++){
            nums[i] = arr[i];
        }
    }
};