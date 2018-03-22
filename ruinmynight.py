import sys
import random

argc = len(sys.argv)

if argc == 2:
    try:
        input = open(sys.argv[1], "r")
    except OSError:
        print("Error opening named file")
        print("Usage: " + sys.argv[0] + " heroes_file [wins_file]")
        exit(1)
    
    heroes = input.readlines()
    heroes = [x.strip() for x in heroes]
    print(random.choice(heroes))
 
elif argc !=3:
    print("Usage: " + sys.argv[0] + " heroes_file [wins_file]")
