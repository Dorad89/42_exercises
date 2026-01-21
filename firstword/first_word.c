/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   first_word.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dulqinak <dulqinak@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/19 22:36:43 by dulqinak          #+#    #+#             */
/*   Updated: 2026/01/19 23:22:13 by dulqinak         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int main(int argc, char **argv)
{
    if (argc != 2)
    {
        write(1, "\n", 1);
        return 0;
    }
    int i = 0;

    while(argv[1][i] == 32 || argv[1][i] == 9)
        i++;

    while((argv[1][i] != 32 && argv[1][i] != 9) && argv[1][i] != '\0')
    {
        write(1, &argv[1][i], 1);
        i++;
    }
    write(1, "\n", 1);
    return 0;
}