class Solution {
public:
    vector<vector<int>> pascalTriangleIII(int n) {
        vector<vector<int>>pascal(n);
        for (int i=0 ; i<n ; i++){
            pascal[i] = vector<int>(i+1,0);
            for (int j=0 ; j<=i ; j++){
                if (j==0 || j==i) pascal[i][j] = 1;
                else {
                    pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j];
                }
            }
        }
        return pascal;
    }
};