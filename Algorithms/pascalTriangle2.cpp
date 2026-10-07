class Solution {
public:
    vector<int> pascalTriangleII(int r) {
        vector<vector<int>>pascal(r, vector<int>(r, 0));
        for (int i=0 ; i<r ; i++){
            for (int j=0 ; j<=i ; j++){
                if (j==0 || j==i) pascal[i][j] = 1;
                else {
                    pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j];
                }
            }
        }

        vector<int> ans(r,0);
        for (int i=0 ; i<r ; i++){
            ans[i] = pascal[r-1][i];
        }
        return ans;
    }
};