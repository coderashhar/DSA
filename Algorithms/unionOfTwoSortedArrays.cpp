class Solution {
public:
    vector<int> unionArray(vector<int>& nums1, vector<int>& nums2) {
        int n1 = nums1.size();
        int n2 = nums2.size();
        int p1 = 0;
        int p2 = 0;
        vector<int> ans;
        for (int i=0 ; i<min(n1,n2) ; i++){
            if (nums1[p1] == nums2[p2]){
                ans[i] = nums1[p1];
                p1++;
                p2++;
            }
            else if (nums[])
        }
    }
};