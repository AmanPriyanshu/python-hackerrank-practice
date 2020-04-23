def print_rangoli(size):
    # your code goes here
    # middle line is the longest, len = ((size-1)*4+1)
    # other than middle, nos. of ---- in LHS is basically: (5 - n)*2
    # -'s of LHS: (5-n)*2
    # output in mid: n...-3-2-1-2-3-...n
    for i in range(1, size+1):
        for j in range(2*(size-i)):
            print('-', end="")
        c = 0
        for j in range(0, i-1):
            print(chr(97+size-1-j)+'-', end="")
            c += 1
        print(chr(97+size-1-c), end="")
        for j in range(1, i):
            print('-'+chr(97+size-i+j), end="")
        for j in range(2*(size-i)):
            print('-', end="")
        print()
    for i in range(size-1, 0, -1):
        for j in range(2*(size-i)):
            print('-', end="")
        c = 0
        for j in range(0, i-1):
            print(chr(97+size-1-j)+'-', end="")
            c += 1
        print(chr(97+size-1-c), end="")
        for j in range(1, i):
            print('-'+chr(97+size-i+j), end="")
        for j in range(2*(size-i)):
            print('-', end="")
        print()


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)