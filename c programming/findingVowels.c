#include<stdio.h>

void countVowel(char vowel[],char str[]){
    printf("Enter the string: ");
    fgets(str,50,stdin);

    int count=0;

    for(int i=0;i<10; i++){
        char check = vowel[i];
        for(int j=0; str[j]!='\0'; j++){
            if(check==str[j]){
                count++;
            }
        }
    }
    printf("The number of vowel appeared in the string is %d",count);

}

int main()
{
    char vowel[] = {'a','e','i','o','u','A','E','I','O','U'};
    char str[50];
    countVowel(vowel,str);
    return 0;
}
