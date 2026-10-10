class Solution{	
	public:		
		bool palindromeCheck(string& s){
			int i = 0;
            int j = s.size() - 1;
            while (i<j){
                if (s[i] == s[j]){
                    i++;
                    j--;
                }
                else return false;

            }
            return true;
		}
};