'''
Created on 10. dec. 2011

@author: niko
'''
import sys
import xml.dom.minidom

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



dataName = ["jos1M-01","jos1M-02","jos1M-03","jos1M-04",
            "jos1M-05","jos1M-06","jos1M-07","jos1M-08","jos1M-09","jos1M-10"]
f = open("C:/users/banic/Desktop/corpus.pos", "w")

for i in dataName:
    IN = "C:/Users/banic/Desktop/jos1M/"+i+".xml"
    doc = xml.dom.minidom.parse(IN)

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