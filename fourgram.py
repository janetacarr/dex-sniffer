__author__ = 'janetacarr'

import sys
import os
import string
import io
import zipfile
import binascii
import dexUtil
import nltk
import methodCounts
from os import walk

fourgramBytes = ['\x02', '\x05', '\x08', '\x13', '\x15', '\x16', '\x1a', '\x1c',
                 '\x1f', '\x20', '\x22', '\x23', '\x29', '\x2d', '\x2e', '\x2f',
                 '\x30', '\x31', '\x32', '\x33', '\x34', '\x35', '\x36', '\x37',
                 '\x38', '\x39', '\x3a', '\x3b', '\x3c', '\x3d', '\x44', '\x45',
                 '\x46', '\x47', '\x48', '\x49', '\x4a', '\x4b', '\x4c', '\x4d',
                 '\x4f', '\x50', '\x51', '\x52', '\x53', '\x54', '\x55', '\x56',
                 '\x57', '\x58', '\x59', '\x5a', '\x5b', '\x5c', '\x5d', '\x5e',
                 '\x5f', '\x60', '\x61', '\x62', '\x63', '\x64', '\x65', '\x66',
                 '\x67', '\x68', '\x69', '\x6a', '\x6b', '\x6c', '\x6d', '\x90',
                 '\x91', '\x92', '\x93', '\x94', '\x95', '\x96', '\x97', '\x98',
                 '\x99', '\x9a', '\x9b', '\x9c', '\x9d', '\x9e', '\x9f', '\xa0',
                 '\xa1', '\xa2', '\xa3', '\xa4', '\xa5', '\xa6', '\xa7', '\xa8',
                 '\xa9', '\xaa', '\xab', '\xac', '\xad', '\xae', '\xaf', '\xd0',
                 '\xd1', '\xd2', '\xd3', '\xd4', '\xd5', '\xd6', '\xd7', '\xd8',
                 '\xd9', '\xda', '\xdb', '\xdc', '\xdd', '\xde', '\xdf', '\xe0',
                 '\xe1', '\xe2']

def isInstructionSetFourgram(fourgrams):
    for j in fourgramBytes:
        if j == fourgrams[1]:
            return True
    return False

def fourgram(author, sample, data):

    print 'Opening fourgrams.txt'
    output = open('/home/rst/datasetprofiles/fourgrams2.txt', 'a+')
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

    codeFourgrams = nltk.ngrams(flatdex[dataOffset:dataOffset+dataSize], 4)

    print "Writing fourgrams\n"
    stuff = list(codeFourgrams)

    instrFourgram = [item for item in sorted(set(stuff)) if isInstructionSetFourgram(item)]

    fourcount = 0
    for item in instrFourgram:
        fourcount = fourcount +1
    #output.write('counts: '+ str(fourcount) + '\n')

    theGrams = [(stuff.count(item), item) for item in instrFourgram]
    topThousand = sorted(theGrams, None, None, True)[0:1000]

    output.write(author + ',' + sample + ',' + methodCounts.sixgram(data) + ',' + str(fourcount) + ',')
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
                print ('/home/rst/datasetprofiles/' + str(i) + '/' + str(file))[:-4]+'fourgrams.txt'
                fourgram(str(i), str(file), '/home/rst/datasetprofiles/' + str(i) + '/' + str(file))

run()