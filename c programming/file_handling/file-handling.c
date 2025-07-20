#include<stdio.h>

int main(){

    // File mode>>>writing
    FILE *file = fopen("example.txt","w");
    if (file!=NULL){
        fprintf(file, "This is an example file");
        fclose(file);
    }

    // File mode>>>Appending
    file = fopen("example.txt","a");
    if (file!=NULL){
        fprintf(file, "This is new text");
        fclose(file);
    }

    // File mode>>>Reading
    file = fopen("example.txt","a");
    if (file==NULL){
        printf("The file doesn't exist");
        fclose(file);
    }else{
        printf("The file exist");
    }
    return 0;
}