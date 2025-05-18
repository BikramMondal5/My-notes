#include<stdio.h>

int main(){
    int element;
    printf("Enter the number of elements in the array: ");
    scanf("%d",&element);
    int a[element];

    for(int i=0; i<element; i++){
        printf("Enter the %d element: ",i+1);
        scanf("%d",&a[i]);
    }
    printf("The elements in the array are:\n");
    for(int i=0; i<element; i++){
        printf("%d\n",a[i]);
    }

    int search;
    printf("Enter the element to be searched: ");
    scanf("%d",&search);

    int count = 0;
    for(int i=0; i<element; i++){
        if(a[i] == search){
            count++;
        }
    }

    printf("The %d appeared in the array is %d times",search,count);
    return 0;
}
