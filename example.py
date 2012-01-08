# -*- coding: utf-8 -*

import pickle
import nltk.data
import time, datetime
from nltk import PunktWordTokenizer

### FUNCTIONS ###
#prettPrint
def prettyPrint(uniResult):
    print ", ".join("(%s | %s)" % (x.decode("utf-8"),y) for (x,y) in uniResult)

def prettyPrintByLine(uniResult):
    for (x,y) in uniResult:
        print "(",x.decode("utf-8")," | ",y,")"

def prettyPrintWithDescription(uniResult, description):
    for (x,y) in uniResult:
	if y in description:
	    print "(",x.decode("utf-8")," | ",y,") - "+unicode(description[y][0],"utf-8")
        else:
	    print "(",x.decode("utf-8")," | ",y,") - ni razlage"

def prettyPrintWithFullDescription(uniResult, description):
    for (x,y) in uniResult:
	if y in description:
	    print "(",x.decode("utf-8")," | ",y,") - "+unicode(description[y][0],"utf-8")+" "+unicode(description[y][1],"utf-8")
        else:
	    print "(",x.decode("utf-8")," | ",y,") - ni razlage"

#slo tag - input UNICODE
def sloTag(uText):
    tokens = PunktWordTokenizer().tokenize(uText)
    result = tagger.tag(tokens)
    return result

#slo tag2 - input UNICODE
def sloTag2(uText):
    sents = sent_tokenizer.tokenize(uText)
    tokens = []
    for s in sents:
        if s[-1] == '.':
            s = s[:-1]+" ."
        t = PunktWordTokenizer().tokenize(s)
        tokens += t
    result = tagger.tag(tokens)
    return result

#get description dictionary for file
def getDict(f):
    dict = {}
    lines = f.readlines()
    for line in lines:
        s = line.split()
        d = ""
        for i in s[2:]:
            d += i+" "
        dict[s[0].upper()] = (s[1],d)
    return dict

#get all description dictionaries
def getExplanationDict():
    dict_sl = getDict( open( "jos1M/josMSD-canon-sl.tbl", "r" ) )
    dict_en = getDict( open( "jos1M/josMSD-canon-en.tbl", "r" ) )
    return dict_sl, dict_en
#################


### USAGE EXAMPLE ###

_t0 = time.time()
#select the tagger
tagger = pickle.load( open("slovene_taggers/TrigramTagger.pickle") )
#tagger = pickle.load( open("slovene_taggers/BrillTagger.pickle") )
#tagger = pickle.load( open("slovene_taggers/NaiveBayes.pickle") )
sent_tokenizer = nltk.data.load('tokenizers/punkt/slovene.pickle')
dict_sl, dict_en = getExplanationDict()
_t1 = time.time()


#uText is input text
uText = 'Lep je dan, vse diši že po pomladi!'
#uText = 'Živé naj vsi naródi, ki hrepené dočakat dan, da, koder sonce hodi, prepir iz svéta bo pregnan, ko rojak prost bo vsak, ne vrag, le sosed bo mejak.'
#uText = 'Potem se je obrnil proti nam in skozi solze izoblikoval najlepši nasmeh, kar sem jih videl v življenju.'


_t2 = time.time()
result = sloTag2(uText)
print result
_t3 = time.time()

prettyPrintWithDescription(result, dict_sl)

print ""
print "Loading time ",time.strftime("%H:%M:%S", time.gmtime(_t1-_t0)), "(",_t1-_t0,"s )"
print "Tagging time ",time.strftime("%H:%M:%S", time.gmtime(_t3-_t2)), "(",_t3-_t2,"s )"
print "Total time   ",time.strftime("%H:%M:%S", time.gmtime(_t3-_t0)), "(",_t3-_t0,"s )"
