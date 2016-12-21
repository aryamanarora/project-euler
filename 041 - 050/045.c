#include <stdio.h>
#include <stdint.h>
#define VALUES 10000

uint64_t pentagonal(uint64_t x)
{
    return (x * (3 * x - 1)) / 2;
}

uint64_t hexagonal(uint64_t x)
{
    return (x * (2 * x - 1));
}

int main(int argc, char const *argv[]) {
    uint64_t pentagon[VALUES];
    uint64_t hexagon[VALUES];
    // make a list of pentagonal and hexagonal numbers
    for (uint64_t i = 0; i < VALUES; i++)
    {
        pentagon[i] = pentagonal(i);
        hexagon[i] = hexagonal(i);
        printf("%lld\n", (char*) hexagon[i]);
    }

    // intersection
    uint64_t j = 0, k = 0;
    while (j < VALUES && k < VALUES)
    {
        if (pentagon[j] < hexagon[k])
            j++;
        else if (pentagon[j] < hexagon[k])
            k++;
        else
            printf("%lld\n", (char*) pentagon[j]);
    }
    return 0;
}
