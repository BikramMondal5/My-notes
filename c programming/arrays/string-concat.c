#include<stdio.h>
#include<string.h>

void my_cat(char str1[], char str2[]){
    int len1 = strlen(str1)-1;
    int len2 = strlen(str1)-1;

    for(int i=0; str2[i]!= '\0'; i++){
        str1[len1+i] = str2[i];
    }
    
    printf("Your new arary is %s", str1);
}

int main(){
    char str1[100];
    char str2[100];
    

    printf("Enter your first string: ");
    fgets(str1,100,stdin);

    printf("Enter your second string: ");
    fgets(str2,100,stdin);

    my_cat(str1,str2);
    return 0;
}