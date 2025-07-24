// 2D Matrix Addition & Multiplication using malloc() and Pointers

#include <stdio.h>
#include <stdlib.h>

// Function to print matrix
void printMatrix(int** matrix, int row, int col) {
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
}

// Function to add two matrices
void addMatrix(int** A, int** B, int row, int col) {
    printf("Addition of matrices:\n");
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            printf("%d ", A[i][j] + B[i][j]);
        }
        printf("\n");
    }
}

// Function to multiply two matrices
void multiplyMatrix(int** A, int** B, int r1, int c1, int c2) {
    printf("Multiplication of matrices:\n");
    for (int i = 0; i < r1; i++) {
        for (int j = 0; j < c2; j++) {
            int sum = 0;
            for (int k = 0; k < c1; k++) {
                sum += A[i][k] * B[k][j];
            }
            printf("%d ", sum);
        }
        printf("\n");
    }
}

int main() {
    int r1, c1, r2, c2;
    printf("Enter rows and columns of matrix A: ");
    scanf("%d %d", &r1, &c1);

    printf("Enter rows and columns of matrix B: ");
    scanf("%d %d", &r2, &c2);

    if (c1 != r2) {
        printf("Matrix multiplication not possible (columns of A != rows of B)\n");
        return 1;
    }

    // Allocate memory for matrices A and B
    int** A = (int**) malloc(r1 * sizeof(int*));
    int** B = (int**) malloc(r2 * sizeof(int*));

    for (int i = 0; i < r1; i++) A[i] = (int*) malloc(c1 * sizeof(int));
    for (int i = 0; i < r2; i++) B[i] = (int*) malloc(c2 * sizeof(int));

    // Input matrix A
    printf("Enter elements of matrix A:\n");
    for (int i = 0; i < r1; i++)
        for (int j = 0; j < c1; j++)
            scanf("%d", &A[i][j]);

    // Input matrix B
    printf("Enter elements of matrix B:\n");
    for (int i = 0; i < r2; i++)
        for (int j = 0; j < c2; j++)
            scanf("%d", &B[i][j]);

    // Print matrices
    printf("Matrix A:\n");
    printMatrix(A, r1, c1);

    printf("Matrix B:\n");
    printMatrix(B, r2, c2);

    // Add matrices if dimensions match
    if (r1 == r2 && c1 == c2)
        addMatrix(A, B, r1, c1);
    else
        printf("Matrix addition not possible (size mismatch).\n");

    // Multiply matrices
    multiplyMatrix(A, B, r1, c1, c2);

    // Free memory
    for (int i = 0; i < r1; i++) free(A[i]);
    for (int i = 0; i < r2; i++) free(B[i]);
    free(A);
    free(B);

    return 0;
}
