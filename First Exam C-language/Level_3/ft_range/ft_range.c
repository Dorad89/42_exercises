#include <stdlib.h>

int *ft_range(int start, int end)
{
    int len = (start <= end) ? (end - start + 1) : (start - end + 1);
    
    int *range;
    range = malloc(sizeof(int) * len);
    if(!range)
        return NULL;

    int i = 0;

    int step = (start <= end) ? 1 : -1;

    while (i < len)
    {   
        range[i] = start;
        i++;
        start += step;
    }
    return range;
}