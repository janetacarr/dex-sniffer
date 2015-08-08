import sys
import string
import io
import zipfile
import binascii
import dexUtil
__author__ = 'janetacarr'



endianness = True

#Get our apk file from the OS
apk = zipfile.ZipFile(sys.argv[1], 'r')

#extract dex file
dex = list(apk.open('classes.dex'))
flatdex = []

#convert dex file to list of bytes
for line in dex:
    for byte in line:
        flatdex.append(byte)


print flatdex[0:104]

if (flatdex[40:44] == ['\x78', '\x56', '\x34', '\x12']):
    print "dex is Big endian"
    endianness = False
else:
    print "dex is litte-endian (default)"

mapOffset = dexUtil.extractValue(flatdex, 48, 4, endianness)
dataOffset = dexUtil.extractValue(flatdex, 108, 4, endianness)
dataSize = dexUtil.extractValue(flatdex, 104, 4, endianness)

print "map offset: " + str(mapOffset)
print "Data offset: " + str(dataOffset)
print "Data size: " + str(dataSize)

print "Begin data section dump:"
#print flatdex[dataOffset:dataOffset+dataSize/2]

i = 0
for byte in flatdex[dataOffset:dataOffset+dataSize/2]:
    if (byte == '\x28'):
        i = i+1

print "gotos: " + str(i)