#include <stdlib.h>

int     *ft_rrange(int start, int end)
{
    int len = (end > start) ? (end - start + 1): (start - end + 1);
    
    int *rrange;
    rrange = malloc(sizeof(int) * len);
    if(!rrange)
        return NULL;

    int step = (start > end) ? -1 : 1;
    while(len > 0)
    {
        rrange[len - 1] =  start;
        start += step;
        len--;
    }
    return rrange;
}