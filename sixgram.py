__author__ = 'janetacarr'
import os
import sys
import zipfile
import dexUtil
import nltk
import methodCounts
from os import walk

sixgramBytes = ['\x03', '\x06', '\x09', '\x14', '\x17', '\x1b', '\x24', '\x25', '\x26',
                '\x2a', '\x2b', '\x2c', '\x6e', '\x6f', '\x70', '\x71', '\x72', '\x74',
                '\x75', '\x76', '\x77', '\x78']

def isInstructionSetSixgram(sixgrams):
    for j in sixgramBytes:
        if j == sixgrams[1]:
            return True

    return False

def sixgram(author, sample, data):

    print 'Opening: sixgrams.txt'
    output = open('/home/rst/datasetprofiles/sixgrams2.txt', 'a+')

    endianness = True

    #Get our apk file from the OS
    apk = zipfile.ZipFile(data, 'r')

    #extract dex file
    dex = list(apk.open('classes.dex'))
    flatdex = []

    #convert dex file to list of bytes
    for line in dex:
        for byte in line:
            flatdex.append(byte)

    if (flatdex[40:44] == ['\x78', '\x56', '\x34', '\x12']):
        #print "dex is Big endian"
        endianness = False

    mapOffset = dexUtil.extractValue(flatdex, 48, 4, endianness)
    dataOffset = dexUtil.extractValue(flatdex, 108, 4, endianness)
    dataSize = dexUtil.extractValue(flatdex, 104, 4, endianness)

    print "map offset: " + str(mapOffset)
    print "Data offset: " + str(dataOffset)
    print "Data size: " + str(dataSize)

    codeSixgrams = nltk.ngrams(flatdex[dataOffset:dataOffset+dataSize], 6)

    print "Writing sixgrams\n"
    stuff = list(codeSixgrams)

    instrSixgram = [item for item in sorted(set(stuff)) if isInstructionSetSixgram(item)]

    sixcount = 0
    for item in instrSixgram:
        sixcount = sixcount +1
    #output.write('count: ' + str(sixcount) + '\n')

    theGrams = [(stuff.count(item), item) for item in instrSixgram]
    topThousand = sorted(theGrams, None, None, True)[0:1000]

    output.write(author + ',' + sample + ',' + methodCounts.sixgram(data) +',' + str(sixcount) + ',')
    for g in topThousand:
        if g != topThousand[999]:
            output.write(str(g)+',')
        else:
            output.write(str(g)+'\n')

    output.close()

def run(datasetprofiles = 0):
    folders = []
    for (dirpath, dirnames, filenames) in walk('/home/rst/datasetprofiles'):
        folders.extend(dirnames)
        break


    for i in folders:
        apks = []
        path = '/home/rst/datasetprofiles/'+str(i)
        for (dirpath, dirnames, filenames) in walk(path):
            apks.extend(filenames)
            break

        for file in apks:
            if (file != '._.DS_Store') and (file != '.DS_Store') and (file[-4:] == '.apk'):
                print '/home/rst/datasetprofiles/' + str(i) + '/' + str(file)
                print ('/home/rst/datasetprofiles/' + str(i) + '/' + str(file))[:-4]+'sixgrams.txt'
                sixgram(str(i), str(file), '/home/rst/datasetprofiles/' + str(i) + '/' + str(file))


run()