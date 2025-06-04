#include <stdio.h>
#include<string.h>

int main() {
    char str[20];
    int count=0,space=0;
    printf("Enter youe name: ");
    fgets(str,20,stdin);
    for(int i=0; str[i]!= '\0'; i++){
       if(str[i]=='a' || str[i]=='e' || str[i]=='i' || str[i]=='o' || str[i]=='u' || str[i]=='A' || str[i]=='E' || str[i]=='I' || str[i]=='O' || str[i]=='U'){
            count++;
        }

        if(str[i]==' '){
            space++;
        }
       
    }

    int len = strlen(str)-1-space;
    int cons = len - count;
    printf("Number of length in the string: %d\n", len);
    printf("Number of vowels in the string: %d\n", count);
    printf("Number of consonent in the string: %d\n", cons);
    printf("Number of spaces in the string: %d\n", space);
    return 0;
}
