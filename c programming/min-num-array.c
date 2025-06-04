#include<stdio.h>

int main(){
    int arr[5] = {34,56,43,12,31};

    int min_num = arr[0];

    for(int i=0; i<5; i++){
        if(arr[i]<min_num){
            min_num = arr[i];
        }
    }

    printf("The min number in the array is: %d",min_num);
    return 0;
}