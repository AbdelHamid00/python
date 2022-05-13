import sys

if(len(sys.argv) != 3):
    print('Usage : python operations <number1> <number2>')
    exit()

if(sys.argv[1].isdigit() and sys.argv[2].isdigit()):
    print('Sum:', int(sys.argv[1]) + int(sys.argv[2]))
    print('Difference:', int(sys.argv[1]) - int(sys.argv[2]))
    print('Product:', int(sys.argv[1]) * int(sys.argv[2]))
    if (int(sys.argv[2]) != 0):
        print('Quotient:', int(sys.argv[1]) / int(sys.argv[2]))
        print('Remainder:', int(sys.argv[1]) % int(sys.argv[2]))
else:
    print('numbers please!')
