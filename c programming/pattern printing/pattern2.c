#include <stdio.h>

int main() {
    int n;
    
    printf("Enter the number of rows: ");
    scanf("%d", &n);
    
    for (int i = 1; i <= n; i++) {
        // Determine number of elements in current row
        int elements;
        if (i == 1) {
            elements = 1;
        } else if (i == 2) {
            elements = 2;
        } else {
            elements = i + 1;
        }
        
        // Print leading spaces for centering
        int spaces = (n + 1) - elements;
        for (int j = 0; j < spaces; j++) {
            printf("  ");
        }
        
        // Determine starting value (alternates each row)
        int start_val = (i % 2 == 1) ? 1 : 0;
        
        // Print the binary pattern for current row
        for (int j = 0; j < elements; j++) {
            if (j == 0) {
                printf("%d", start_val);
            } else {
                printf("   %d", (start_val + j) % 2);
            }
        }
        
        printf("\n");
    }
    
    return 0;
}