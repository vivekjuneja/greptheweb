from lxml import etree
#infile = open("content.example.xml", "r")
#infile.seek(0)
outfile = open("output_test001.txt", "w")
class EchoTarget():
    def start(self, tag, attrib):
        if tag.endswith("xternalPage"):
            line = attrib["about"]
            if line != "":
                try:
                    outfile.write(line+"\n")
                except:
                    pass
            print line
    def close(self):
        return "closed!"
parser = etree.XMLParser(target = EchoTarget())
result = etree.parse("content.rdf.u8.xml", parser)