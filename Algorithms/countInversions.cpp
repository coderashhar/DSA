class Solution {
public:
    long long int merge(vector<int>& arr, int low, int mid, int high) {
        
        // Temporary array for merging
        vector<int> temp;
        
        // Starting indices of left and right halves
        int left = low;
        int right = mid + 1;
 
        // Count variable to count the pairs
        long long int cnt = 0;
 
        // Merge sorted halves into temp array
        while (left <= mid && right <= high) {
            if (arr[left] <= arr[right]) {
                
                temp.push_back(arr[left]);
                left++;
                
            } 
            else {
                temp.push_back(arr[right]);
                
                // Count inversions
                cnt += (mid - left + 1);
                
                right++;
            }
        }
 
        // Copy remaining elements of left half
        while (left <= mid) {
            temp.push_back(arr[left]);
            left++;
        }
 
        // Copy remaining elements of right half
        while (right <= high) {
            temp.push_back(arr[right]);
            right++;
        }
 
        /* Copy elements from temp 
        array back to original array*/
        for (int i = low; i <= high; i++) {
            arr[i] = temp[i - low];
        }
        
        //return the count of inversions
        return cnt;
    }
    long long int mergesort(vector<int>& arr, int low, int high){
        long long int cnt = 0;
        if (low < high){
            int mid = low + (high - low) / 2;
            cnt += mergesort(arr, low, mid);
            cnt += mergesort(arr, mid+1, high);
            cnt += merge(arr, low, mid, high);
        }
        return cnt;
    }
    long long int numberOfInversions(vector<int> nums) {
        int n = nums.size();
        return mergesort(nums, 0, n-1);
    }
};