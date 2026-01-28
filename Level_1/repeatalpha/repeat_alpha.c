#include <unistd.h>

int main(int argc, char **argv)
{
    if (argc == 2)
    {
        int i = 0;
        while(argv[1][i])
        {
            if(argv[1][i] >= 65 && argv[1][i] <= 90)
            {
                int repeat = argv[1][i] - 64;
                while (repeat > 0)
                {
                    write(1, &argv[1][i], 1);
                    repeat--;
                }
            }
            else if(argv[1][i] >= 97 && argv[1][i] <= 122)
            {
                int repeat = argv[1][i] - 96;
                while (repeat > 0)
                {
                    write(1, &argv[1][i], 1);
                    repeat--;
                }
            }
            else 
                write(1, &argv[1][i], 1);
            i++;
        }
    }
    write(1, "\n", 1);
}