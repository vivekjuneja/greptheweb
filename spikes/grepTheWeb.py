from lxml import etree
from StringIO import StringIO

hexatrimalChars = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
head = ""

def tailgen():
        for i in range(0,36):
                tail=hexatrimalChars[i]
                domain=head+tail
                print domain

tailgen()
for count in range(0,36):
        head=head+hexatrimalChars[count]
        tailgen()

#def tailgenerator(head, tail):
#        for num in range(tail,10):
#            domain = head+str(num)
#            return domain
#        for i in range(len(alphabet)):
#            domain = head+alphabet[i]
#            return domain

#print tailgenerator(head, tail)
#tail +=1
#print tailgenerator(head, tail)

#incrementor(head)

#for num in range(0,10):
#    head = str(num)
#    incrementor(head)
#for i in range(len(alphabet)):
#    head = alphabet[i]
#    incrementor(head)
#
#for num in range(0,10):
#    head = str(num)
#    for num in range(0,10):
#        penHead = str(num)
#        incrementor(head+penHead)
#    for i in range(len(alphabet)):
#        penHead = alphabet[i]
#        incrementor(head+penHead)
#for i in range(len(alphabet)):
#    head = alphabet[i]
#    for num in range(0,10):
#        penHead = str(num)
#        incrementor(head+penHead)
#    for i in range(len(alphabet)):
#        penHead = alphabet[i]
#        incrementor(head+penHead)
