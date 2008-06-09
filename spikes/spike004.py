def seq():
    theseq = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', \
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', \
       'k',  'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', \
        'u', 'v', 'w', 'x', 'y', 'z']
       
    tempstring = '0'
    yield tempstring
       
    while True:
        if not tempstring[-1] == 'z':
            lastchar = theseq[theseq.index(tempstring[-1])+1]
            tempstring = ''.join([i for i in tempstring[:-1]])
            tempstring += lastchar
        else:
            try:
                tempchar = tempstring[-2]
            except:
                tempchar = tempstring[-1]
            counter = 0
            if not tempchar == 'z':
                while not tempchar == 'z':
                    counter += 1
                    try:
                        tempchar = tempstring[-(counter+1)]
                    except:
                        break
                tempchar = theseq[theseq.index(tempchar)+1]
                tempstring = ''.join([i for i in tempstring[:-(counter)]])
                tempstring += tempchar
                tempstring += '0'*(counter-1)
            else:
                tempstring = ''.join(['0' for i in tempstring])
                tempstring += '0'
        yield tempstring
       
if __name__ == '__main__':
    gen = seq()
    for x in xrange(8888):
        print str(x)+" "+gen.next()
