#include <iostream>
using namespace std;

void reverse(int arr[], int l, int r){
	if (l >= r) return;
	int temp = arr[r];
	arr[r] = arr[l];
	arr[l] = temp;
	reverse(arr, l+1, r-1);
}

int main(){
	int arr[5] = {1,2,3,4,5};
	reverse(arr, 0, 4);
	for (int i=0; i<5; i++) { cout<<arr[i]<<","; }
	return 0;
}

