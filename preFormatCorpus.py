'''
Created on 10. dec. 2011

@author: niko
'''
import sys
import xml.dom.minidom

if len(sys.argv) != 3:
    print "TWO ARGUMENTS NEEDED!"
    print "    First is the path for input file"
    print "    Second is the paht for output file"
    sys.exit()
IN = sys.argv[1]
OUT = sys.argv[2]

data = xml.dom.minidom.parse(IN)
print "Reading of input xml finsihed."

i = 1
#for all sentences
for sentances in data.getElementsByTagName("s"):
    print "Sentence: ",i
    i += 1
    print sentances.toprettyxml()
