class Solution{	
	public:		
		void reverseString(vector<char>& s){
			vector<char>res;
            for (int i=s.size()-1 ; i>=0 ; i--){
                res.push_back(s[i]);
            }
            s.assign(res.begin(), res.end());
		}
};