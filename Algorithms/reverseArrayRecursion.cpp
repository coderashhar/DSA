#include <iostream>
using namespace std;

void reverse(int arr[], int i, int n){
	if (i >= n-i-1) return;
	int temp = arr[i];
	arr[i] = arr[n-i-1];
	arr[n-i-1] = temp;
	reverse(arr, i+1, n);
}

int main(){
	int arr[5] = {1,2,3,4,5};
	cout<<"original array: ";
	for (int i=0; i<5; i++){ cout<<arr[i]<<","; }
	reverse(arr, 0, 5);
	cout<<"reversed array: ";
        for (int i=0; i<5; i++){ cout<<arr[i]<<","; }
	return 0;
}
