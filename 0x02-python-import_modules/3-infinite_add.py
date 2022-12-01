#!/usr/bin/python3
import sys
if __name__ == '__main__':
    av = sys.argv
    len_av = len(av)
    add = 0
    if len_av > 1:
        for i in range(1, len_av):
            add += int(av[i])
    print(add)
