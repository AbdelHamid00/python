import sys

if (len(sys.argv) > 2):
    print('Usage: python whois.py <number>')
    quit()
if (len (sys.argv) == 1):
    print()
    quit()
x = sys.argv[1].isdigit()
if(x == True):
    a = int(sys.argv[1])
    if (a == 0):
        print('I m Zero.')
    elif (a % 2 == 0):
        print('I m Even.')
    else :
        print('I m Odd.')
else :
    print('Error : argument is not integer')
