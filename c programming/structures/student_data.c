#include<stdio.h>
#include<string.h>

struct student{
    char name[100];
    int roll;
    float cgpa;
};

int main()
{
    struct student s1;
    strcpy(s1.name, "Bikram Mondal");
    s1.roll = 12;
    s1.cgpa = 9.3;

    printf("Student: %s\n",s1.name);
    printf("Roll no: %d\n",s1.roll);
    printf("CGPA: %.2f\n",s1.cgpa);

    struct student s2;
    strcpy(s2.name, "Arijit Sarkar");
    s2.roll = 21;
    s2.cgpa = 9.7;

    printf("Student: %s\n",s2.name);
    printf("Roll no: %d\n",s2.roll);
    printf("CGPA: %.2f\n",s2.cgpa);

    struct student s3;
    strcpy(s3.name, "Koushik Ghosh");
    s3.roll = 11;
    s3.cgpa = 9.7;

    printf("Student: %s\n",s3.name);
    printf("Roll no: %d\n",s3.roll);
    printf("CGPA: %.2f\n",s3.cgpa);

    return 0;
}