#include <stdio.h>


int a = 1;
int j = 2;


int maximum(int a, int b) {
	if (a > b){ return a; }
	else { return b; } 
}

/*
int maximum2(int a, int b) {
	if (a>b) return a;
	else return b;
}

int some_array[5] = (1, 2, 1, 4, 5);
*/
int some_ar[5];

int print_ar(int an_array[]) {
	int i, sum=0;
	for(i = 0; i<5; i++)
		sum = sum + an_array[i];
}


int main() {
	printf("Blah: %d\n",a);
	printf("Max %d, %d is: %d",a,j,maximum(a,j));
	
	return 0; }

