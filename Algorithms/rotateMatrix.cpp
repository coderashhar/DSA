class Solution {
public:
    void rotateMatrix(vector<vector<int>>& matrix) {
        int n = matrix.size();
        vector<vector<int>>res(n, vector<int>(n,0));
        for (int i=0 ; i<n ; i++){
            for (int j=0 ; j<n ; j++){
                int r = n-j-1;
                res[i][j] = matrix[r][i];
            }
        }
        for (int i=0 ; i<n ; i++){
            for (int j=0 ; j<n ; j++){
                matrix[i][j] = res[i][j];
            }
        }
    }
};