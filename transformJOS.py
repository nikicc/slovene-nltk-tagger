import sys
import os
import xml.dom.minidom

out = "jos1M.pos"
out = os.path.join("pos", out)

dataName = ["jos1M-01.xml","jos1M-02.xml","jos1M-03.xml",
"jos1M-04.xml","jos1M-05.xml","jos1M-06.xml",
"jos1M-07.xml","jos1M-08.xml","jos1M-09.xml",
"jos1M-10.xml"]

f = open(out, "w")

for i in dataName:
    IN = "jos1M/"+i
    doc = xml.dom.minidom.parse(IN)
    print "Finished parsing: "+IN

    #for all sentences
    for sentances in doc.getElementsByTagName("s"):
         for i in sentances.childNodes:
            if i.nodeName != "#text":
                if i.nodeName == "S":
                    f.write(" ")
                elif(i.nodeName == "term"):
                    parseTerm(i.childNodes)
                elif(i.nodeName == "c"):

                    f.write(" ")
                    f.write((i.firstChild.data).encode('utf8'))
                    f.write("/")
                    f.write((i.firstChild.data).encode('utf8'))

                    f.write(" ")



                elif (i.nodeName == "w"):
                    f.write((i.firstChild.data +"/"+ str(i.getAttribute("msd"))).encode('utf8'))
         f.write("\n")
    print "Finished transforming: "+IN
f.close()
print "The transformed corpus is in file: "+out


# term parsing
def parseTerm(childrenT):
     for j in childrenT:
        if j.nodeName != "#text":
            if j.nodeName == "S":
                f.write(" ")
            elif(j.nodeName == "c"):

                f.write(" ")
                f.write((j.firstChild.data).encode('utf8'))
                f.write("/")
                f.write((j.firstChild.data).encode('utf8'))
                f.write(" ")


            elif (j.nodeName == "w"):
                f.write((j.firstChild.data +"/"+ str(j.getAttribute("msd"))).encode('utf8'))
