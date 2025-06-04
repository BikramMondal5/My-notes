#include <stdio.h>

#define ROWS 3
#define COLS 4

// Function to calculate and print sum of each row
void rowSums(int arr[ROWS][COLS]) {
    for (int i = 0; i < ROWS; i++) {
        int sum = 0;
        for (int j = 0; j < COLS; j++) {
            sum += arr[i][j];
        }
        printf("Sum of row %d = %d\n", i + 1, sum);
    }
}

// Main function
int main() {
    int arr[ROWS][COLS];

    // Input values
    printf("Enter elements of %d x %d matrix:\n", ROWS, COLS);
    for (int i = 0; i < ROWS; i++) {
        for (int j = 0; j < COLS; j++) {
            printf("Element [%d][%d]: ", i, j);
            scanf("%d", &arr[i][j]);
        }
    }

    // Call function to compute row sums
    printf("\nRow-wise sums:\n");
    rowSums(arr);

    return 0;
}
