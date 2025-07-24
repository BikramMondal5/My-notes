#include <stdio.h>
#include <time.h>

long long int fibrec(int n)
{
    if (n == 0)
        return 0;
    else if (n == 1)
        return 1;
    else
        return fibrec(n - 1) + fibrec(n - 2);
}

long long int fibitr(int n)
{
    if (n == 0)
        return 0;
    else if (n == 1)
        return 1;

    long long int fib[n + 1];  // Create array to store Fibonacci numbers
    fib[0] = 0;
    fib[1] = 1;

    for (int i = 2; i <= n; i++)
    {
        fib[i] = fib[i - 1] + fib[i - 2];
    }

    return fib[n];  // Return the nth Fibonacci number
}

int main()
{
    time_t start_time, finish_time;
    double timeDiff;
    long long int a, b, n;

    printf("Enter no. of terms: ");
    scanf("%lld", &n);

    time(&start_time);
    a = fibrec(n);
    time(&finish_time);
    printf("The fibonacci number by recursive is: %lld \n", a);
    timeDiff = difftime(finish_time, start_time);
    printf("It is taking %f seconds to execute \n", timeDiff);

    time(&start_time);
    b = fibitr(n);
    time(&finish_time);
    printf("The fibonacci number by iterative using array is: %lld \n", b);
    timeDiff = difftime(finish_time, start_time);
    printf("It is taking %f seconds to execute \n", timeDiff);

    return 0;
}
