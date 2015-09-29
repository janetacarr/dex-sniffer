__author__ = 'janetacarr'
import sys
import zipfile
import dexUtil
import nltk
import os
import methodCounts
from os import walk


digramBytes = ['\x00', '\x01', '\x04', '\x07', '\x0a', '\x0b', '\x0c', '\x0d', '\x0e', '\x0f', '\x10', '\x11', '\x12', '\x1d', '\x1e', '\x21', '\x27', '\x28',
               '\x73', '\x7b', '\x7c', '\x7d', '\x7e', '\x7f', '\x80', '\x81', '\x82', '\x83', '\x84', '\x85', '\x86', '\x87', '\x88', '\x89', '\x8a', '\x8b',
               '\x8c', '\x8d', '\x8e', '\x8f', '\xb0', '\xb1', '\xb2', '\xb3', '\xb4', '\xb5', '\xb6', '\xb7', '\xb8', '\xb9', '\xba', '\xbb', '\xbc', '\xbd',
               '\xbe', '\xbf', '\xc0', '\xc1', '\xc2', '\xc3', '\xc4', '\xc5', '\xc6', '\xc7', '\xc8', '\xc9', '\xca', '\xcb', '\xcc', '\xcd', '\xce', '\xcf']

def isInstructionSetDigram(digram):
    for j in digramBytes:
        if j == digram[1]:
            return True
    return False

def digram(author, sample, data):
    #print 'Creating: ' + str(data[:-4])+'digrams.txt'
    #output = open(str(data[:-4])+'digrams.txt', 'w+')

    print 'Opening: digrams.txt'
    output = open('/home/rst/datasetprofiles/digrams2.txt', 'a+')

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

    #print flatdex[0:104]
    if (flatdex[40:44] == ['\x78', '\x56', '\x34', '\x12']):
        #print "dex is Big endian"
        endianness = False

    mapOffset = dexUtil.extractValue(flatdex, 48, 4, endianness)
    dataOffset = dexUtil.extractValue(flatdex, 108, 4, endianness)
    dataSize = dexUtil.extractValue(flatdex, 104, 4, endianness)

    print "map offset: " + str(mapOffset)
    print "Data offset: " + str(dataOffset)
    print "Data size: " + str(dataSize)

    codeDigrams = nltk.ngrams(flatdex[dataOffset:dataOffset+dataSize], 2)

    print "Writing digrams\n"
    stuff = list(codeDigrams)
    # dicount = 0
    # for item in set(stuff):
    #     dicount = dicount +1
    # print dicount

    instrDigram = [item for item in sorted(set(stuff)) if isInstructionSetDigram(item)]

    dicount = 0
    for item in instrDigram:
        dicount = dicount +1
    #output.write('count: ' + str(dicount) + '\n')

    theGrams = [(stuff.count(item), item) for item in instrDigram]
    topThousand = sorted(theGrams, None, None, True)[0:1000]

    output.write(author + ',' + sample + ',' + methodCounts.sixgram(data) +',' + str(dicount) + ',')
    for g in topThousand:
        if g != topThousand[999]:
            output.write(str(g[1][0])+str(g[1][1])+',')
        else:
            output.write(str(g[1][0])+str(g[1][1])+'\n')

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
                print ('/home/rst/datasetprofiles/' + str(i) + '/' + str(file))[:-4]+'digrams.txt'
                digram(str(i), str(file), '/home/rst/datasetprofiles/' + str(i) + '/' + str(file))

run()
