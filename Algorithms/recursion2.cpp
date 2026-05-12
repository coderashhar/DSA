#include <iostream>
using namespace std;

void printnum(int i, int n){
	if (i>n) return;
	cout<<i<<endl;
	printnum(i+1, n);
}

int main(){
	printnum(1,10);
	return 0;
}
