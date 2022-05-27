#include <stdio.h>

int get_fib_at_n(int n) {
    if (n == 0) {
        return 0;
    } else if (n == 1) {
        return 1;
    } else {
        return get_fib_at_n(n-1) + get_fib_at_n(n-2);
    }
}

void main() {
    int n = 7;
    int fib = get_fib_at_n(n);

    printf("%i\n", fib);
}