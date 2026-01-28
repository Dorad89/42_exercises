#include <unistd.h>

int main(int argc, char **argv)
{
    if (argc == 2)
    {
        int i = 0;
        int len = 0;
        while(argv[1][len])
            len++;
        while(i <= len / 2)
        {
            char temp = argv[1][i];
            argv[1][i] = argv[1][len - i - 1];
            argv[1][len - i - 1] = temp;
            i++;
        }
        int j = 0;
        while(argv[1][j])
        {
            write(1, &argv[1][j], 1);
            j++;
        }
    }
    write(1, "\n", 1);
}