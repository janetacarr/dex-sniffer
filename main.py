__author__ = 'janetacarr'

import sys
import os
import zipfile
import dexUtil
import digram
import fourgram
import sixgram



def main():

    endianness = True

    #Get our apk file from the OS
    data = sys.argv[1]
    apk = zipfile.ZipFile(data, 'r')

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

    MethodCalls = 0
    for l in flatdex[dataOffset:dataOffset+dataSize]:
        if((l == '\x6e') or (l == '\x6f') or (l == '\x70') or (l == '\x71') or (l == '\x72')  or (l == '\x74') or (l == '\x76') or (l == '\x77') or (l == '\x78')):
            MethodCalls = MethodCalls + 1

    print "Number of externel library calls: " + str(MethodCalls) + "\n"

    #trigram.trigram(data)
    # fourgram.fourgram(data)
    # fivegram.fivegram(data)
    # sixgram.sixgram(data)
    #os.wait()

main()