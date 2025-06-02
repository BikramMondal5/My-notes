#include <stdio.h>

int main() {
    int n;
    
    printf("Enter the number of rows (odd number): ");
    scanf("%d", &n);
    
    // First row - all stars
    for (int j = 0; j < 2 * n - 1; j++) {
        printf("* ");
    }
    printf("\n");
    
    // Middle rows - hollow pattern
    for (int i = 1; i < n; i++) {
        int stars_each_side = n - i;
        int spaces_between = 2 * i - 1;
        
        // Left side stars
        for (int j = 0; j < stars_each_side; j++) {
            printf("* ");
        }
        
        // Spaces in between
        for (int j = 0; j < spaces_between; j++) {
            printf("  ");
        }
        
        // Right side stars
        for (int j = 0; j < stars_each_side; j++) {
            printf("* ");
        }
        
        printf("\n");
    }
    
    return 0;
}