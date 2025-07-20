// Write a C program that accepts an integer from the user and prints the next five prime numbers in sequence

#include <stdio.h>

int main() {
    int num, count = 0;

    printf("Enter the number: ");
    scanf("%d", &num);

    for (int i = num + 1; ; i++) {
        int isPrime = 1;

        if (i <= 1) {
            isPrime = 0;
        } else {
            for (int j = 2; j * j <= i; j++) {
                if (i % j == 0) {
                    isPrime = 0;
                    break;
                }
            }
        }

        if (isPrime) {
            printf("%d ", i);
            count++;
        }

        if (count == 5) {
            break;
        }
    }

    printf("\n");
    return 0;
}
