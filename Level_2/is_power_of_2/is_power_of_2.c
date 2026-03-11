int	    is_power_of_2(unsigned int n)
{
        while(n % 2 == 0)
            n /= 2;
        return (n == 1);
}