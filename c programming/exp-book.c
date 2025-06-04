#include<stdio.h>

struct  book{
    char title[100];
    char author[100];
    float price;
};

int main(){
    int num,maxIndex=0;
    printf("Enter the number of books: ");
    scanf("%d", &num);
    getchar();

    struct  book s[num];

    for(int i=0; i<num; i++){
        printf("Enter the title of the book%d: ",i+1);
        fgets(s[i].title, sizeof(s[i].title), stdin);

        printf("Enter the author of the book%d: ",i+1);
        fgets(s[i].author, sizeof(s[i].title), stdin);

        printf("Enter the price of the book%d: ",i+1);
        scanf("%f", &s[i].price);
        getchar();
    }

    for(int i=0; i<num; i++){
        if(s[i].price > s[maxIndex].price){
            maxIndex = i;
        }
    }

    
    printf("The details for the most expensive book: \n");
    printf("%s",s[maxIndex].title);

    printf("%s",s[maxIndex].author);

    printf("%f",s[maxIndex].price);
    

    
    return 0;
}