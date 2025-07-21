#include<stdio.h>

int main(){
    int a, b, c, max;
    printf("Enter the numbers: ");
    scanf("%d %d %d", &a, &b, &c);

    // Using If-else statement
    max = a;
    if(max<b){
        max = b;
    }
    
    if(max<c){
        max = c;
    }

    printf("%d",max);

    // Using ternary number
    max = (a>b) ? (a>c ? a:c) : (b>c ? b:c);

    printf("%d",max);
    return 0;
}