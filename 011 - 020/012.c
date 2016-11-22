#include <stdio.h>
#include <math.h>

int factors(int num);

int triangle(void);

int main(int argc, char const *argv[])
{
    /* triangle generator */
    int n = 1;
    int triangle[20000];
    while (n < 20000) {
        triangle[n] = (n * (n + 1)) / 2;
        n++;
    }

    /* looks through the list */
    for (int i = 1; i < 20000; i++)
    {
        if (factors(triangle[i]) > 500)
        {
            printf("The first triangle number with 500 factors is %i\n", triangle[i]);
            break;
        }
    }
}

int factors(int num)
{
    int factors = 1;
    if (num % 2 == 0)
    {
        for (int i = 1; i < ceil(sqrt(num)); i++)
        {
            if (num % i == 0)
                factors += 2;
        }
    }
    return factors;
}
