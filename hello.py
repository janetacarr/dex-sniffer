import sys
import string
import io
__author__ = 'janetacarr'

print "hello project!"

dex = io.FileIO(sys.argv[1], 'r', True)
#dex = open(inputFile, 'r')

lst = list(dex)
print lst[0:8]