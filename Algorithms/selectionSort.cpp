class Solution {
public:
    vector<int> selectionSort(vector<int>& nums) {
        int n = nums.size();
        for (int i=0 ; i<n ; i++){
            int smallestidx = i;
            for (int j=i+1 ; j<n ; j++){
                if (nums[j] < nums[smallestidx]) smallestidx = j;
            }
            if (i != smallestidx) swap(nums[i], nums[smallestidx]);
        }
        return nums;
    }
};
