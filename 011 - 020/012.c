#include <stdio.h>

int factors(int num);

int main(int argc, char const *argv[])
{
    int i = 1;
    int j = 1;
    while (factors(i) < 510)
    {
        if (factors(i) > 100)
        {
            printf("%i %i", i, factors(i));
        }
        j++;
        i += j;
    }
    return 0;
}

int factors(int num)
{
    int results = 2;
    if (num % 2 == 0)
    {
        for (int i = 2; (i < num / 2) + 1; i++)
        {
            if (num % i == 0)
                results++;
        }
    }
    else
    {
        for (int i = 3; i < (num / 2); i += 2)
        {
            if (num % i == 0)
                results++;
        }
    }
    return results;
}
