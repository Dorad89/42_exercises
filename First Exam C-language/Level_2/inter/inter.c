#include <unistd.h>

int main(int argc, char **argv)
{
    if (argc == 3)
    {
        int i = 0;
        int j;
        int check[256] = {0};

        while(argv[1][i])
        {
            j = 0;
            while(argv[2][j])
            {
                if(argv[1][i] == argv[2][j] && !check[(unsigned char)argv[1][i]])
                {
                    write(1, &argv[1][i], 1);
                    check[(unsigned char)argv[1][i]] = 1;
                    break;
                }
                j++;
            }
            i++;
        }

    }
    write(1, "\n", 1);
    return (0);
}