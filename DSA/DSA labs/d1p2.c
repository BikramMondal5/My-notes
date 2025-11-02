// WAP to display a complex no. using pointers.
#include<stdio.h>

struct complex{
    float real;
    float imag;
};

int main(){
    struct complex z, *pz;
    pz = &z;

    z.real = 1.5;
    z.imag = 3.5;

    printf("Complex number using pointer: %.1f + %.1fi\n", pz->real, pz->imag);

    return 0;
}
