#include <iostream>
using namespace std;

int sumn(int n){
	if (n<1) return 0;
	return (n + sumn(n-1));
}

int main(){
	int n;
	cout<<"enter number: ";
	cin>>n;
	cout<<"sum: "<<sumn(n);
	return 0;
}

