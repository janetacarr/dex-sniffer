__author__ = 'janetacarr'

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

opBytes = [GOTO, GOTO16, GOTO32, PSWITCH, SSWITCH, IF_EQ, IF_NE, IF_LT, IF_GE, IF_GT, IF_LE, IF_EQZ, IF_NEZ, IF_LTZ, IF_GEZ, IF_GTZ, IF_LEZ, IN_VIRTUAL, IN_SUPER, IN_DIRECT, IN_STATIC, IN_INTERFACE, IN_VIRTUALR, IN_SUPERR, IN_DIRECTR, IN_STATICR,IN_INTERFACER]

