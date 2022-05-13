import sys

if (len(sys.argv) != 3):
    print("Run it in this way : python3 filterwords.py [string] [number]")
    exit()
if (sys.argv[2].isnumeric() == False):
    print("Run it in this way : python3 filterwords.py [string] [number]")
tab = sys.argv[1].split

