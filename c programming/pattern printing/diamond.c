#include <stdio.h>

int main() {
    int n;
    int attempts = 0;
    int max_attempts = 3;
    
    while (attempts < max_attempts) {
        printf("Enter the number of rows: ");
        scanf("%d", &n);
        
        // Check if number is odd
        if (n % 2 == 1) {
            break; // Valid odd number, exit the loop
        } else {
            attempts++;
            printf("Error: Please enter an odd number.\n");
            
            if (attempts < max_attempts) {
                printf("You have %d attempt(s) remaining.\n", max_attempts - attempts);
            }
        }
    }
    
    // If all attempts failed, terminate
    if (attempts == max_attempts) {
        printf("All attempts failed. Program terminated.\n");
        return 1;
    }
    
    // Print the diamond pattern
    int mid = n / 2; // Middle row index
    
    for (int i = 0; i < n; i++) {
        int stars;
        
        // Calculate number of stars for current row
        if (i <= mid) {
            // Upper half (including middle)
            stars = 2 * i + 1;
        } else {
            // Lower half
            stars = 2 * (n - i - 1) + 1;
        }
        
        // Calculate spaces for centering
        int spaces = (n - stars) / 2;
        
        // Print leading spaces
        for (int j = 0; j < spaces; j++) {
            printf(" ");
        }
        
        // Print stars with spaces between them
        for (int j = 0; j < stars; j++) {
            printf("*");
            if (j < stars - 1) {
                printf(" ");
            }
        }
        
        printf("\n");
    }
    
    return 0;
}