from os import walk

def isAscii(character):
    if character == '\\':
        return False
    if ord(character) >= 0x20 or ord(character) <= 0x7e:
        return True


def fixFormat(author, sample, path):
    f = open(path, 'r')
    input = list(f)
    output = open('/home/rst/datasetprofiles/MethodCounts.txt', 'a+')

    methodCount=0
    try:
        diff = (len(input[0])-15)
        methodCount = int(input[0][-diff:])
    except(IndexError):
        print IndexError.message
    output.write(author + ',' + sample + ',' + str(methodCount))
    print author + ',' + sample + ',' + str(methodCount)

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

    output = open('/home/rst/datasetprofiles/MethodCounts.txt', 'a+')
    output.write("author, sample, methodCalls\n")
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
            if (file != '._.DS_Store') and (file != '.DS_Store') and (file[-16:] == 'methodCounts.txt'):
                print '/home/rst/datasetprofiles/' + str(i) + '/' + str(file)
                #print ('/home/rst/datasetprofiles/' + str(i) + '/' + str(file))[:-4]+'digrams.txt'
                fixFormat(str(i), str(file), '/home/rst/datasetprofiles/' + str(i) + '/' + str(file))

run()