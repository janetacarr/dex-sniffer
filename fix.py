__author__ = 'janetacarr'

from os import walk

def isAscii(character):
    if character == '\\':
        return False
    if ord(character) >= 0x20 or ord(character) <= 0x7e:
        return True


def fixFormat(author, sample, path):
    input = list(open(path, 'r'))
    output = open('/home/rst/datasetprofiles/digrams.txt', 'a+')

    bytelist = []
    first = True
    place = 0
    i = 0

    output.write(author+','+sample+',')

    diff = (len(input[0])-7)
    methodCount = int(input[0][-diff:])

    for line in input[1:100]:
        bytelist = []
        for byte in line:
            if byte != '(' and byte != ')' and byte != ',' and byte != ' ' and byte != '\'' and byte != '\n':
                bytelist.append(byte)
        i = i + 1

        bytestring = ''
        commas = 0
        for c in bytelist[0:8]:
            bytestring = bytestring + c

        if isAscii(bytestring[0]):
            c = bytestring[0].encode("hex")
            bytestring = "\\x" + c + bytelist[4] + bytelist[5] + bytelist[6] + bytelist[7]
        if isAscii(bytestring[4]):
            c = bytestring[4].encode("hex")
            bytestring = bytestring[0:4] + "\\x" + c

        if(i == len(input)-1):
            output.write(bytestring+'\n')
        else:
            output.write(bytestring + ',')


    output.close()

#output = open("/home/rst/datasetprofiles/digrams3.txt", 'a+')
#for line in bytestring:
 #   output.write(line)

#output.close()

#print bytelist
    #print bytestring
    #print bytestring[place]

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
            if (file != '._.DS_Store') and (file != '.DS_Store') and (file[-11:] == 'digrams.txt'):
                print '/home/rst/datasetprofiles/' + str(i) + '/' + str(file)
                #print ('/home/rst/datasetprofiles/' + str(i) + '/' + str(file))[:-4]+'digrams.txt'
                fixFormat(str(i), str(file), '/home/rst/datasetprofiles/' + str(i) + '/' + str(file))

run()