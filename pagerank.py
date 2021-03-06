#!/usr/bin/env python

"""
    Google Toolbar 3.0.x/4.0.x Pagerank Checksum Algorithm

    Author's webpage:
        http://pagerank.gamesaga.net/
"""

def  IntStr(String, Integer, Factor):
    for i in range(len(String)) :
        Integer *= Factor
        Integer &= 0xFFFFFFFF
        Integer += ord(String[i])
    return Integer


def HashURL(Str):
    C1 = IntStr(Str, 0x1505, 0x21)
    C2 = IntStr(Str, 0, 0x1003F)

    C1 >>= 2
    C1 = ((C1 >> 4) & 0x3FFFFC0) | (C1 & 0x3F)
    C1 = ((C1 >> 4) & 0x3FFC00) | (C1 & 0x3FF)
    C1 = ((C1 >> 4) & 0x3C000) | (C1 & 0x3FFF)

    T1 = (C1 & 0x3C0) << 4
    T1 |= C1 & 0x3C
    T1 = (T1 << 2) | (C2 & 0xF0F)

    T2 = (C1 & 0xFFFFC000) << 4
    T2 |= C1 & 0x3C00
    T2 = (T2 << 0xA) | (C2 & 0xF0F0000)

    return (T1 | T2)


def CheckHash(HashInt):
    HashStr = "%u" % (HashInt)
    Flag = 0
    CheckByte = 0

    i = len(HashStr) - 1
    while i >= 0:
        Byte = int(HashStr[i])
        if 1 == (Flag % 2):
            Byte *= 2;
            Byte = Byte / 10 + Byte % 10
        CheckByte += Byte
        Flag += 1
        i -= 1

    CheckByte %= 10
    if 0 != CheckByte:
        CheckByte = 10 - CheckByte
        if 1 == Flag % 2:
            if 1 == CheckByte % 2:
                CheckByte += 9
            CheckByte >>= 1

    return '7' + str(CheckByte) + HashStr

def RetPr(URL):
    import urllib
    hsh = CheckHash(HashURL(URL))
    gurl = 'http://toolbarqueries.google.com/tbr?client=navclient-auto&ch=%s&features=Rank&q=info:%s' % (hsh,urllib.quote(URL))
    
    f = urllib.urlopen(gurl)
    st = f.read()
    st = st.lstrip().rstrip()
    st = st[9:]
    try:
        st = int(st)
    except:
        st = 0
    
    return st
    

def RetTic(URL):
    import urllib
    yurl = 'http://bar-navig.yandex.ru/u?ver=2&show=32&url=%s' % URL
    
    f = urllib.urlopen(yurl)
    st = f.read()
    import re
    m = re.search(r'value="([0-9]{1,5})"', st)
    
    try:
        tic = m.group(1)
    except:
        tic = 0;
    
    return tic


def RetYaca(URL):
    import urllib
    yurl = 'http://testsitedaily.com' % URL
    
    f = urllib.urlopen(yurl)
    st = f.read()
    import re
    m = re.search(r'<textinfo>(?P<author>[\W\w]+)</textinfo>', st)
    
    try:
        yaca = m.group(1)
    except:
        yaca = '';
    
    if len(yaca) > 2:
        return 'y'
    else:
        return 'n'


if __name__ == '__main__':
    import sys
    import urllib
    if len(sys.argv) < 3:
        print 'No URL specified.'
        sys.exit()
    
    if sys.argv[1] == 'PR':
        print RetPr(sys.argv[2])
    if sys.argv[1] == 'TYC':
        print RetTic(sys.argv[2])
    if sys.argv[1] == 'YACA':
        print RetYaca(sys.argv[2])