#include <stdio.h>

void passByVal(int val); // pass in copy of the integer
void passByRef(int & ref); // pass a reference to the variable (i.e. the actual variable)
void passByPtr(int * ptr); // pass a pointer to the variable

int main() {
	int x = 5;
	printf("x = %i\n", x);
	passByVal(x);
	printf("x = %i\n", x);
	passByRef(x);
	printf("x = %i\n", x);
	passByPtr(&x);
	// equivalently
	int * xptr = &x;
	printf("*xptr = %i\n", *xptr);
	passByPtr(xptr);
	printf("*xptr = %i\n", *xptr);
	printf("x = %i\n", x);
	return 0;
}

void passByVal(int val) {
	val = 10;
	printf("val = %i\n", val);
}

void passByRef(int & ref) {
	ref = 20;
	printf("ref = %i\n", ref);	
}

void passByPtr(int * ptr) {
	*ptr = 30;
	printf("*ptr = %i\n", *ptr);
}
