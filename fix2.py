__author__ = 'rst'

__author__ = 'janetacarr'

from os import walk

def isAscii(character):
    if character == '\\':
        return False
    if ord(character) >= 0x20 or ord(character) <= 0x7e:
        return True


def fixFormat(author, sample, path):
    f = open(path, 'r')
    input = list(f)
    output = open('/home/rst/datasetprofiles/fourgrams.txt', 'a+')

    bytelist = []
    first = True
    place = 0
    i = 0




    diff = (len(input[0])-7)
    methodCount = int(input[0][-diff:])

    output.write(author + ',' + sample + ',' + str(methodCount) + ',')

    for line in input[1:1001]:
        bytelist = []
        for byte in line:
            if byte != '(' and byte != ')' and byte != ',' and byte != ' ' and byte != '\'' and byte != '\n':
                bytelist.append(byte)
        i = i + 1

        bytestring = ''
        commas = 0
        for c in bytelist[0:16]:
            bytestring = bytestring + c
        try:
            if isAscii(bytestring[0]):
                c = bytestring[0].encode("hex")
                bytestring = "\\x" + c + bytelist[4] + bytelist[5] + bytelist[6] + bytelist[7]
            if isAscii(bytestring[4]):
                c = bytestring[4].encode("hex")
                bytestring = bytestring[0:4] + "\\x" + c

            #print bytestring

            if(i == len(input)-1):
                output.write(bytestring)
            else:
                output.write(bytestring + ',')

        except:
            pass
        # if(i == 1000):
        #     output.write(bytestring+'\n')
        # else:
        #     output.write(bytestring + ',')
    output.write('\n')
    f.close()
    output.close()

#output = open("/home/rst/datasetprofiles/digrams3.txt", 'a+')
#for line in bytestring:
 #   output.write(line)

#output.close()

#print bytelist
    #print bytestring
    #print bytestring[place]

def run(datasetprofiles = 0):

    output = open('/home/rst/datasetprofiles/fourgrams.txt', 'a+')
    for i in range(0, 992):
        if i == 991:
            output.write("column" + str(i)+"\n")
        else:
            output.write("column" + str(i) + ",")
    output.close()

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
            if (file != '._.DS_Store') and (file != '.DS_Store') and (file[-13:] == 'fourgrams.txt'):
                print '/home/rst/datasetprofiles/' + str(i) + '/' + str(file)
                #print ('/home/rst/datasetprofiles/' + str(i) + '/' + str(file))[:-4]+'digrams.txt'
                fixFormat(str(i), str(file), '/home/rst/datasetprofiles/' + str(i) + '/' + str(file))

run()