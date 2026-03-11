#include <stdlib.h>

char	*ft_itoa(int nbr)
{
    int n = nbr;
    int len = (n <= 0);
    char *str;

    if (n == -2147483648)
    {
        str = malloc(12);
        if (!str)
            return (NULL);
        str[0] = '-'; str[1] = '2'; str[2] = '1'; str[3] = '4';
        str[4] = '7'; str[5] = '4'; str[6] = '8'; str[7] = '3';
        str[8] = '6'; str[9] = '4'; str[10] = '8'; str[11] = '\0';
        return (str);
    }

    while(nbr)
    {
        len++;
        nbr /= 10;
    }

    str = malloc(len + 1);
    if (!str)
        return NULL;
    str[len] = '\0';

    if (n < 0)
    {
        str[0] = '-';
        n = -n;
    }

    if(n == 0)
        str[0] = '0';

    while(n > 0)
    {
        str[--len] = (n % 10) + '0';
        n /= 10;
    }
    return str;
}