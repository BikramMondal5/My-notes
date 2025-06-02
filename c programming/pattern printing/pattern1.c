#include <stdio.h>

int main() {
    int n;
    
    printf("Enter the number of rows: ");
    scanf("%d", &n);
    
    for (int i = 0; i < n; i++) {
        // Print leading spaces for centering
        for (int j = 0; j < i; j++) {
            printf("  ");
        }
        
        // Print characters from Z going inward
        for (int j = 0; j < n - i; j++) {
            printf("%c ", 'Z' - j);
        }
        
        // Print characters from the center going back to Z (excluding the center character)
        for (int j = n - i - 2; j >= 0; j--) {
            printf("%c ", 'Z' - j);
        }
        
        printf("\n");
    }
    
    return 0;
}