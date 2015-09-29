__author__ = 'janetacarr'
import dexUtil
import zipfile
import sys

#Control flow operators, format : syntax .  format reference http://source.android.com/devices/tech/dalvik/instruction-formats.html
GOTO = '\x28' # 10t : goto +AA
GOTO16 = '\x29' # 20t : goto/16 +AAAA
GOTO32 = '\x2a' # 30t : goto/32 +AAAAAAAAA
PSWITCH = '\x2b'# 31t : packed-switch vAA, +BBBBBBBB
SSWITCH = '\x2c'# 31t : sparse-switch vAA, +BBBBBBBB

IF_EQ = '\x32' # 22t : if-test vA, vB, +CCCC
IF_NE = '\x33'
IF_LT = '\x34'
IF_GE = '\x35'
IF_GT = '\x36'
IF_LE = '\x37'

IF_EQZ = '\x38' # 21T if-testz vAA, +BBBB
IF_NEZ = '\x39'
IF_LTZ = '\x3a'
IF_GEZ = '\x3b'
IF_GTZ = '\x3c'
IF_LEZ = '\x3d'

IN_VIRTUAL = '\x6e' # 35c : invoke-kind{vC, vD, vE, vF, vG}, meth@BBBB
IN_SUPER = '\x6f'
IN_DIRECT = '\x70'
IN_STATIC = '\x71'
IN_INTERFACE = '\x72'

IN_VIRTUALR = '\x74' # 3rc : invoke-kind/range{vCCCC .. vNNNN} meth@BBBB
IN_SUPERR = '\x75'
IN_DIRECTR = '\x76'
IN_STATICR = '\x77'
IN_INTERFACER = '\x78'

opBytes = [GOTO, GOTO16, GOTO32, PSWITCH, SSWITCH,
           IF_EQ, IF_NE, IF_LT, IF_GE, IF_GT, IF_LE,
           IF_EQZ, IF_NEZ, IF_LTZ, IF_GEZ, IF_GTZ,
           IF_LEZ, IN_VIRTUAL, IN_SUPER, IN_DIRECT,
           IN_STATIC, IN_INTERFACE, IN_VIRTUALR,
           IN_SUPERR, IN_DIRECTR, IN_STATICR, IN_INTERFACER]

endianness = True

data = sys.argv[1]

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


instructionOffset = 0
instructionNodes = []

#handle individual branch instructions here
def handleInstruction(byte):
    pass


for b in flatdex[dataOffset:dataOffset+dataSize]:
    for item in opBytes:
        if item == b:
            handleInstruction(b)
    instructionOffset = instructionOffset + 1

instructionNodes = set(instructionNodes)

#Find out adjacent nodes.
def adjacentNodes():
    for node in instructionNodes:
        pass

#Create edge set
def findEdges():
    pass

#Label function for edges
def labelFunction((source, dest)):
    pass