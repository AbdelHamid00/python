import sys

if (len(sys.argv) != 2):
    print('deux arguments pas plus ni moins')
tab = sys.argv[1] [::-1]
print(tab.swapcase())
