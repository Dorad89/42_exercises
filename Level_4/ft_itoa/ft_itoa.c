char	*ft_itoa(int nbr)
{
    long n = nbr;
    int len = (n <= 0);
    char *str;

    while(nbr)
    {
        len++;
        nbr /= 10;
    }

    str = malloc(len + 1);
    if(!str)
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