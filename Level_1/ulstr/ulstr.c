#include <unistd.h>

int main(int argc, char **argv)
{
    if(argc == 2)
    {
        while(*argv[1])
        {        
            if (*argv[1] >= 65 && *argv[1] <= 90)
                *argv[1] += 32;
            else if (*argv[1] >= 97 && *argv[1] <= 122)
                *argv[1] -= 32;
            write(1, argv[1]++, 1);
        }
    }
    write(1, "\n", 1);
}