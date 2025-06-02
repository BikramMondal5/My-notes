#include<stdio.h>


void is_spy(int num){
    int sum=0, product=1;
    while(num!=0){
        int digit = num%10;
        sum = sum + digit;
        product = product*digit;
        num = num/10;
    }

    if(sum==product){
        printf("It is a spy number\n");

    }else{
        printf("It is not a spy number");
    }
}

// int is_prime(num){

// }

// int is_palindrome(num){

// }
int main(){
    int choice,num;
    printf("Menu driven program: \n");
    printf("1. Check whether a number is a Spy Number or not\n2. Check whether a number is prime or not\n3. Check whether a number is a palindrome or not\n");
    printf("Enter your choice: ");
    scanf("%d", &choice);

    printf("Enter the number to check: ");
    scanf("%d", &num);
    switch(choice){
        case 1:
            is_spy(num);    
            break;
        case 2:
            // is_prime(num);
            printf("Enter a number to check if it is prime: ");
            break;
        case 3:
            printf("Enter a number to check if it is a palindrome: ");
            // is_palindrome(num);
            break;
        default:
            printf("Invalid input");
    }
    return 0;
}