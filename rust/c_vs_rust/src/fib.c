#include <stdio.h>

void main() {
	int index = 45;
	int value = fib_switch(index);
	printf("%i\n", value);
}

int fib(int index) {
	if(index == 0) {
		return 0;
	} else if (index == 1) {
		return 0;
	} else if (index == 2) {
		return 1;
	} else {
		return fib(index - 1) + fib(index - 2);
	}
}

int fib_switch(int index) {
    switch (index) {
        case 0:
            return 0;
            break;
        case 1:
            return 0;
            break;
        case 2:
            return 1;
            break;
        default:
            return fib_switch(index - 1) + fib_switch(index - 2);
    }
}