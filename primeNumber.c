// To check whether the number is prime or not

#include <stdio.h>

int main() {
    int num, isPrime = 1;
    printf("Enter the number: ");
    scanf("%d", &num);

    if (num <= 1) {
        isPrime = 0;
    } else {
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                isPrime = 0;
                break; // Exit loop early if not prime
            }
        }
    }

    if (isPrime) {
        printf("Prime number");
    } else {
        printf("Not a prime number");
    }

    return 0;
}
