// Write a program to print the max number in an array
#include<stdio.h>

int main(){
    int num;
    printf("Enter the number of element: ");
    scanf("%d",&num);

    int arr[num];
   

    for(int i=0; i<num; i++){
        printf("Enter the element %d: ",i+1);
        scanf("%d",&arr[i]);
    }
    int max=arr[0];

    printf("Your original array is: \n");
    for(int i=0; i<num; i++){
        printf("%d\n",arr[i]);
    }

    for(int i=0; i<num; i++){
        if(max<arr[i]){
            max = arr[i];
        }
    }
    printf("%d is the maximum element in the array",max);
    return 0;
}