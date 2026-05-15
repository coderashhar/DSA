#include <iostream>
using namespace std;

bool isPalindrome(char str[], int l, int r){
	if (str[l] != str[r]) return false;
	if ( l+1 == r || l == r ) return true;
	return isPalindrome(str, l+1, r-1);
}

int main(){
	char str[]  = "aabbaa";
	char str2[] = "madam";	
	char str3[] = "aaabbb";
	char str4[] = "aaabb";
	cout<<isPalindrome(str, 0, 5)<<endl;
	cout<<isPalindrome(str2, 0, 4)<<endl;
	cout<<isPalindrome(str3, 0, 5)<<endl;
	cout<<isPalindrome(str4, 0, 4)<<endl;
	return 0; 
}

	
