// create 1D array using malloc() and pointers in C

#include <stdio.h>
#include <stdlib.h>

// Function to print the array
void printArray(int* arr, int n) {
    printf("Array elements are:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", *(arr + i));  // pointer notation
    }
    printf("\n");
}

int main() {
    int n;
    printf("Enter size of array: ");
    scanf("%d", &n);

    // Allocate memory
    int* arr = (int*) malloc(n * sizeof(int));
    if (arr == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    // Input elements
    printf("Enter %d elements:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", arr + i);  // pointer notation
    }

    // Print array
    printArray(arr, n);

    // Free memory
    free(arr);
    return 0;
}
