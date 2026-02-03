#include <unistd.h>

int main(int argc, char **argv)
{
    if(argc == 2)
    {
        int len = 0;
        while(argv[1][len])
            len++;

        while(len > 0 && (argv[1][len - 1] == 32 || argv[1][len - 1] == 9))
            len--;

        int end = len;

        while(len > 0 && argv[1][len - 1] != 32 && argv[1][len - 1] != 9)
            len--;

        while(len < end)
        {
            write(1, &argv[1][len], 1);
            len++;
        }
    }
    write(1, "\n", 1);
    return 0;
}