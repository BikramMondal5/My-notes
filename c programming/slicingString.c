#include<stdio.h>
#include<string.h>

void slice(char str[], int m, int n){
    
    char new_str[20];
    int j=0;

    for(int i=m; i<=n; i++){
        new_str[j] = str[i];
        j++;
    }
    new_str[j] = '\0';
    printf("%s",new_str);
}
int main()
{
    int m,n;
    char str[20];
    fgets(str,20,stdin);
    printf("Enter the first index: ");
    scanf("%d",&m);

    printf("Enter the second index: ");
    scanf("%d",&n);
    slice(str,m,n);
    return 0;
}
