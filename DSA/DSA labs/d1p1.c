#include<stdio.h>

struct complex{
    float real;
    float imaginary;
};

struct complex addition(struct complex c1, struct complex c2, struct complex result){
    result.real = c1.real + c2.real;
    result.imaginary = c1.imaginary + c2.imaginary;
    return result;
}

struct complex subtract(struct complex c1, struct complex c2, struct complex result){
   result.real = c1.real - c2.real;
    result.imaginary = c1.imaginary - c2.imaginary;
    return result;
}

struct complex multiplication(struct complex c1, struct complex c2, struct complex result){
   result.real = (c1.real * c2.real) - (c1.imaginary * c2.imaginary);
   result.imaginary = (c1.real * c2.imaginary) + (c1.imaginary * c2.real);
   return result;
}

struct complex division(struct complex c1, struct complex c2, struct complex result){
   float deno = (c2.real * c2.real) + (c2.imaginary * c2.imaginary);
   if(deno == 0){
       printf("Division by zero is not possible.\n");
    }else{
        result.real = ((c1.real * c2.real) + (c1.imaginary * c2.imaginary))/deno;
        result.imaginary = ((c1.imaginary * c2.real) - (c1.real * c2.imaginary))/deno;
    
        return result;
    }
   
}

void  display(struct complex result){
    printf("The required result is %0.2f + %0.2f i\n", result.real, result.imaginary);
}

int main(){
    struct complex c1, c2, result;
    printf("Enter the real & imaginary part for the complex no.1: ");
    scanf("%f %f", &c1.real, &c1.imaginary);
    
    printf("Enter the real & imaginary part for the complex no.2: ");
    scanf("%f %f", &c2.real, &c2.imaginary);
    
    int choice;
    
 do{    
    printf("-------Menu-Driven-Program-------\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. To Exit\n");
    printf("Enter the no. of choice: ");
    scanf("%d",&choice);
    
    switch(choice){
        case 1:     result = addition(c1,c2,result);
                    display(result);
                    break;
                    
        case 2:     result = subtract(c1,c2,result);
                    display(result);
                    break;
                    
        case 3:     result = multiplication(c1,c2,result);
                    display(result);
                    break;
    
        case 4:     result = division(c1,c2,result);
                    display(result);
                    break;

        case 5:     printf("Exiting the program...\n");
                    break;

       default:    printf("Invalid input!");
    }
  }while(choice!=5);
  
    return 0;
}
