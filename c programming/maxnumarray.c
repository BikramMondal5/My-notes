#include<stdio.h>

int main(){
    int arr[5] = {34,56,43,12,31};

    int max_num = arr[0];

    for(int i=0; i<5; i++){
        if(arr[i]>max_num){
            max_num = arr[i];
        }
    }

    printf("The maximum number in the array is: %d",max_num);
    return 0;
}