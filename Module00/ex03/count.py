import sys
import string

if (len(sys.argv) != 2):
    print('Error : just one argument please.')
    quit()

s = 0
u = 0
l = 0
p = 0
for i in sys.argv[1]:
    if(i.isupper()):
        u = u + 1
    elif(i.islower()):
        l = l + 1
    elif i in string.punctuation:
        p = p + 1
    elif(i.isspace()):
        s = s + 1
print('- ', u ,'upper letters')
print('- ', l ,'lower letters')
print('- ', p ,'punctuation maks')
print('- ', s ,'spaces')