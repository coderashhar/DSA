#include <iostream>
using namespace std;

void printname(int i, int n){
	if (i>n) return;
	cout<<"Ashhar";
	printname(i+1,n);
}

int main(){
	int n;
	cout<<"enter no. of times:";
	cin>>n;
	printname(1,n);
	return 0;
}


