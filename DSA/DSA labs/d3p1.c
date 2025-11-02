#include<stdio.h>
#include<stdlib.h>

void printArray(int* arr, int n){
    printf("The elements present in the array: ");
    for(int i=0; i<n; i++){
        printf("%d ", *(arr+i));
    }
}
int main(){
    int n;
    printf("Enter the size of the array: ");
    scanf("%d",&n);

    int* arr = (int*)malloc(n*sizeof(int));

    // Taking inputs
    printf("Enter the elements to be inserted.\n");
    for(int i=0; i<n; i++){
        printf("Element %d: ", i+1);
        scanf("%d", (arr + i));
    }

    printArray(arr,n);
    free(arr);
    return 0;
}

// (arr+i): address of the ith element and *(arr+i): value at the ith element address.
