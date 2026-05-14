#include <iostream>
using namespace std;

int sum(int sm, int n){
	if (n < 1) return sm;
	return sum(sm+n, n-1);
}

int main(){
	int sm = 0;
	int n;
	cout<<"enter n:";
	cin>>n;
	if (n==0) return 0;
	sm = sum(sm,n);
	cout<<"sum of first n numbers is : "<<sm;
}
