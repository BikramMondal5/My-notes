#include<stdio.h>

int main()
{
    int num;
    printf("Enter the number of elements present in the array: ");
    scanf("%d",&num);
    int arr[num];

    for(int i=0; i<num; i++){
        printf("Enter the %d element: ",i+1);
        scanf("%d",&arr[i]);
    }
    printf("Your original array is: \n");
    for(int i=0; i<num; i++){ 
        
        printf("%d\n",arr[i]);
    }                         
      
    for(int i=0; i<num/2; i++){
        int firstValue = arr[i];
        int secondValue = arr[num-i-1];
        arr[i] = secondValue;
        arr[num-i-1] = firstValue;
    }

    printf("Your reversed array is: \n");
    for(int i=0; i<num; i++){
        printf("%d\n",arr[i]);
    }

    return 0;
}