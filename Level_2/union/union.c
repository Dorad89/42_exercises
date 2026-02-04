#include <unistd.h>

int main(int argc, char **argv)
{
    if(argc == 3)
    {
        int j = 0;
        char check[256] = {0};

        while(argv[1][j])
        {
            if(!check[(unsigned char) argv[1][j]])
            {            
                write(1, &argv[1][j], 1);
                check[(unsigned char) argv[1][j]] = 1;
            }
            j++;
        }

        j=0;
        while(argv[2][j])
        {
            if(!check[(unsigned char) argv[2][j]])
            {            
                write(1, &argv[2][j], 1);
                check[(unsigned char) argv[2][j]] = 1;
            }
            j++;
        }
    }
    write(1, "\n", 1);
    return (0);
}