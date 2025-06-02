// To check whether the number given by the user is perfect number or not. A perfect number is a positive number in which sum of all positive divisors excluding that number is equal to that number. For example, 6 is a perfect number because its divisors are 1, 2, and 3, and their sum is 6 (1 + 2 + 3 = 6)

#include <stdio.h>

int main() {
    int num, sum = 0;

    // Get the number from the user
    printf("Enter a number: ");
    scanf("%d", &num);

    // Check if the number is positive
    if (num <= 0) {
        printf("Error: The number must be positive.\n");
    }

    // Find the sum of all positive divisors excluding the number itself
    for (int i = 1; i < num; i++) {
        if (num % i == 0) {
            sum += i;
        }
    }

    // Check if the sum is equal to the number
    if (sum == num) {
        printf("%d is a perfect number.\n", num);
    } else {
        printf("%d is not a perfect number.\n", num);
    }

    return 0;
}
