import sys
import string
__author__ = 'janetacarr'

print "hello project!"

inputFile = sys.argv[1]
dex = open(inputFile, 'r')
for line in dex:
    print line + '\n'