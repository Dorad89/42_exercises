
#include <stdio.h>

int is_space(int c)
{
    return((c >= 9 && c <=13) || c == 32 ? 1 : 0);
}

int isdigit(int c)
{
    return(c >= 48 && c <=57 ? 1 : 0);
}

int	ft_atoi(const char *str)
{
    int res = 0;
    int i = 0;
    int s = 1;

    while (is_space(str[i]))
        i++;

    if(str[i] == '-')
    {
        s = -1;
        i++;
    }

    while(isdigit(str[i]))
    {
        res *=10;
        res += (str[i] - 48);
        i++;
    }

    return (res * s);
}

int main(int argc, char **argv)
{
    if (argc == 2)
        printf("%d\n", ft_atoi(argv[1]));
    else
        printf("Usage: %s <number>\n", argv[0]);
    return 0;
}