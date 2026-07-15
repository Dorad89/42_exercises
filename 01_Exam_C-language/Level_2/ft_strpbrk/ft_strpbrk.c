char	*ft_strpbrk(const char *s1, const char *s2)
{
    size_t i = 0;
    size_t j;

    while(s1[i])
    {
        j = 0;
        while(s2[j])
        {
            if (s1[i] == s2[j])
                return (char *)&s1[i];
            j++;
        }
        i++;
    }
    return NULL;
}