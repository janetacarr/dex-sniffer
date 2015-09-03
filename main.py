import sys
import string
import io
import zipfile
import binascii
import dexUtil
import nltk

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
    i = i + 1
    if (byte == '.CODE'):
        break

print "gotos: " + str(i)

#bytes = nltk.word_tokenize(''.join(flatdex[i:dataSize]))

codeTrigrams = nltk.trigrams(flatdex[dataOffset:dataSize])
codeFourgrams = nltk.ngrams(flatdex[dataOffset:dataSize], 4)
codeFivegrams = nltk.ngrams(flatdex[dataOffset:dataSize], 5)
codeSixgrams = nltk.ngrams(flatdex[dataOffset:dataSize], 6)

print "Dump Trigrams:\n"
stuff = list(codeTrigrams)
tricount = 0
for item in set(stuff):
    tricount = tricount +1
print tricount
#print [(item, stuff.count(item)) for item in sorted(set(stuff))]


print "\nDump fourgrams\n"
stuff = list(codeFourgrams)
fourcount = 0
for item in set(stuff):
    fourcount = fourcount +1
print fourcount

MethodCalls = 0
for l in flatdex[dataOffset:dataSize]:
    if((l == '\x6e') or (l == '\x6f') or (l == '\x70') or (l == '') or (l == '\x71') or (l == '\x72') or (l == '\x73') or (l == '\x74') or (l == '\x76') or (l == '\x77') or (l == '\x78')):
        MethodCalls = MethodCalls + 1


print [(item, stuff.count(item)) for item in sorted(set(stuff))]


print "\nDump fivegrams\n"
stuff = list(codeFivegrams)
fivecount = 0
for item in set(stuff):
    fivecount = fivecount +1
print fivecount
#print [(item, stuff.count(item)) for item in sorted(set(stuff))]

print "\nDump sixgrams\n"
stuff = list(codeSixgrams)
sixcount = 0
for item in set(stuff):
    sixcount = sixcount +1
print sixcount
#print [(item, stuff.count(item)) for item in sorted(set(stuff))]


print "Total n-grams: " + str(( fourcount + tricount)) + "\n"
print "Number of externel library calls: " + str(MethodCalls) + "\n"