n=7
for row in range(0,n):
    if (row ==0) or (row==n-1):
        print("*"*7)
    else:
        print(" " * (n-row-1) + "*")


def pattern1(n):
    for i in range(0,n):
        for j in range( ord('A'), ord('A') +
                              (2 * n) - 1):
            if j >= (ord( 'A' ) + n - 1) + i:
                print(chr((ord('A') + n - 1) -
                  (j % (ord('A') + n - 1))), end = '')
             
            elif j <= (ord('A') + n - 1) - i:
                print(chr(j), end = '')
            else:
                print(end = " ")
        print("\n", end = '')
    for i in range(n-2,-1,-1):
        for j in range( ord('A'), ord('A') +
                              (2 * n) - 1):
            if j >= (ord( 'A' ) + n - 1) + i:
                print(chr((ord('A') + n - 1) -
                  (j % (ord('A') + n - 1))), end = '')
             
            elif j <= (ord('A') + n - 1) - i:
                print(chr(j), end = '')
            else:
                print(end = " ")
        print("\n", end = '')


n = 6
pattern1(n)
