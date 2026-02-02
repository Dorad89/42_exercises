size_t	ft_strspn(const char *s, const char *accept)
{
    size_t i = 0;
    while(s[i])
    {
        size_t j = 0;
        size_t res = 0;
        while (accept[j])
        {
            if(s[i] == accept[j])
            {                
                res = 1;
                break;
            }
            j++;
        }
        if(res == 0)
            return i;
        i++;
    }
    return (i);
}