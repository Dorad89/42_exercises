char    *ft_strdup(const char *src)
{
    size_t int i = 0;
    size_t int len = 0;
    char *res;

    while(src[len])
        len++;
    res = malloc(sizeof(char) * (len + 1));
    if(!res)
        return NULL;
    while(src[i])
    {
        res[i] = src[i];
        i++;
    }
    res[i] = '\0';
    return res;
}