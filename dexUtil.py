__author__ = 'janetacarr'

import struct

#extractValue extracts an integer value from a flatdex (list of bytes in dex file)
#from the offset given. Default assumptions is 4 bytes in length and littleEndian
def extractValue(dex, offset, bytes = 4, littleEndian = True):
    if(littleEndian):
        value = dex[offset+3] + dex[offset+2] + dex[offset+1] + dex[offset]
        return struct.unpack("<L", value)[0]
    else:
        value = dex[offset] + dex[offset+1] + dex[offset+2] + dex[offset+3]
        return struct.unpack("<L", value)[0]