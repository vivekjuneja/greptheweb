from lxml import etree
from StringIO import StringIO

domain = ""
length = 1

def baseconvert(n, base):
    """convert positive decimal integer n to equivalent in another base (2-36)"""

    digits = "0123456789abcdefghijklmnopqrstuvwxyz"

    try:
        n = int(n)
        base = int(base)
    except:
        return ""
    
    if n < 0 or base < 2 or base > 36:
        return ""

    s = ""
    while 1:
        r = n % base
        s = digits[r] + s
        n = n / base
        if n == 0:
            break

    return s

def prefixZeros(inStr, num):
        result = str(inStr)
        if int(num) > 0:
                for i in range(len(str(inStr)),int(num)):
                        result="0"+result
        return result

# print prefixZeros(baseconvert(2590, 36),3)

while domain != "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz":
    for i in range(0,36):
        domain = baseconvert(i, 36)
        print domain
        i +=1