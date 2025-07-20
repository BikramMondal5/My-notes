// Write a program to take input from user and print its length
// Length of a string === No. of characters appeared in the string

#include<stdio.h>

int main()
{
    char name[20];
    int length=0;
    printf("Enter your name: ");
    fgets(name,20,stdin);
    printf("Your name is %s",name);
    for(int i=0; name[i]!='\0'; i++){
        length++;
    }
    length = length - 1;
    printf("The number of character appeared in your text is %d",length);
    return 0;
}