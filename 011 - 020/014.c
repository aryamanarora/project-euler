/**
 * None of this works, and I don't know why...
 */

#include <stdio.h>

int main(void)
{
    long result = 0;
    printf("%li", result);
    for (long i = 0; i < 1000000; i++)
    {
        long collatz = 0;
        long original_num = i;
        long modified_num = i;

        while (modified_num != 1)
        {
            if (modified_num % 2 == 0)
            {
                modified_num /= 2;
            }
            else
            {
                modified_num = (3 * modified_num) + 1;
            }

            collatz += 1;
        }

        if (collatz > result)
        {
            result = collatz;
            printf("%li %li", original_num, collatz);
        }
    }
    return 0;
}
