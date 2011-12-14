'''
Created on 10. dec. 2011

@author: niko
'''
import sys
import xml.dom.minidom
'''
if len(sys.argv) != 3:
    print "TWO ARGUMENTS NEEDED!"
    print "    First is the path for input file"
    print "    Second is the paht for output file"
    sys.exit()

IN = sys.argv[1]
OUT = sys.argv[2]
'''

IN = "C:/Users/banic/Desktop/jos100kv2_0.xml"
OUT ="C:/users/banic/Desktop/test"
doc = xml.dom.minidom.parse(IN)
f = open("C:/users/banic/Desktop/test", "w")


# term parsing
def parseTerm(childrenT):
     for j in childrenT:
        if j.nodeName != "#text":
            if j.nodeName == "S":
                f.write(" ")
            elif(j.nodeName == "c"):
                #print "Character",j.tagName, j.firstChild.data
                f.write((j.firstChild.data).encode('utf8'))
                f.write("/")
                f.write((j.firstChild.data).encode('utf8'))
            elif (j.nodeName == "w"):
                #print j.getAttribute("msd"), j.tagName, j.firstChild.data
                f.write((j.firstChild.data +"/"+ str(j.getAttribute("msd"))).encode('utf8'))

#for all sentences
for sentances in doc.getElementsByTagName("s"):
     for i in sentances.childNodes:
        if i.nodeName != "#text":
            if i.nodeName == "S":
                f.write(" ")
            elif(i.nodeName == "term"):
                parseTerm(i.childNodes)
            elif(i.nodeName == "c"):
                #print "Character",i.tagName, i.firstChild.data
                f.write((i.firstChild.data).encode('utf8'))
                f.write("/")
                f.write((i.firstChild.data).encode('utf8'))
            elif (i.nodeName == "w"):
                #print i.getAttribute("msd"), i.tagName, i.firstChild.data
                #string =str(i.firstChild.data) +"/"+ i.getAttribute("msd")
                f.write((i.firstChild.data +"/"+ str(i.getAttribute("msd"))).encode('utf8'))
     f.write("\n")
f.close()