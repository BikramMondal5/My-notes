#include<stdio.h>
#include<string.h>

struct student{
    char name[100];
    int roll;
    float cgpa;
};

int main()
{
    struct student AIML[71];
    AIML[0].roll = 12;
    AIML[0].cgpa = 9.3;
    strcpy(AIML[0].name, "Bikram Mondal");

    AIML[1].roll = 11;
    AIML[1].cgpa = 9.6;
    strcpy(AIML[1].name, "Koushik Ghosh");

    AIML[2].roll = 21;
    AIML[2].cgpa = 9.6;
    strcpy(AIML[2].name, "Arijit Sarkar");

    printf("Name: %s\n", AIML[0].name);
    printf("Roll: %d\n", AIML[0].roll); 
    printf("CGPA: %.2f\n", AIML[0].cgpa);

    printf("Name: %s\n", AIML[1].name);
    printf("Roll: %d\n", AIML[1].roll);
    printf("CGPA: %.2f\n", AIML[1].cgpa);

    printf("Name: %s\n", AIML[2].name);
    printf("Roll: %d\n", AIML[2].roll);
    printf("CGPA: %.2f\n", AIML[2].cgpa);
    return 0;
}