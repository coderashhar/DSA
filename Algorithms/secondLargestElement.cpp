class Solution {
public:
    int secondLargestElement(vector<int>& nums) {
        int largest = nums[0];
        int secondLargest = -1e5;
        for (int i=1 ; i<nums.size() ; i++){
            if (nums[i] > largest && largest > secondLargest){
                    secondLargest = largest;
                    largest = nums[i];
            }
            else if (nums[i] < largest && nums[i] > secondLargest){
                secondLargest = nums[i];
            }
        }
        if (secondLargest == -1e5) return -1;
        return secondLargest;
        
    }
};