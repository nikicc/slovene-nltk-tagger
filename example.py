# -*- coding: utf-8 -*
import pickle
import nltk.data
import time, datetime
from nltk import PunktWordTokenizer

### FUNCTIONS ###
#prettPrint
def prettyPrint(uniResult):
    print ", ".join("('%s', %s)" % a for a in uniResult)

def prettyPrintByLine(uniResult):
    for a in uniResult:
        print "('%s', %s)" % a

def prettyPrintWithDescription(uniResult, description):
    for (x,y) in uniResult:
	if y in description:
            print "('",x,"', ",y,") - "+description[y][0]
        else:
	    print "('",x,"', ",y,") - ni razlage"

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
#tagger = pickle.load(open("slovene_taggers/TrigramTagger.pickle"))
#tagger = pickle.load(open("slovene_taggers/BrillTagger.pickle"))
tagger = pickle.load(open("slovene_taggers/NaiveBayes.pickle"))
sent_tokenizer=nltk.data.load('tokenizers/punkt/slovene.pickle')
dict_sl, dict_en = getExplanationDict()
_t1 = time.time()


#uText is input text
#uText = u'Lep je dan, vse diši že po pomladi!'
#uText = u'Tistega (većera) sem-preveč "popil", zgodilo se je mesec dni po tem, ko sem izvedel, da me žena vara.'
uText = u'Živé naj vsi naródi, ki hrepené dočakat dan, da, koder sonce hodi, prepir iz svéta bo pregnan, ko rojak prost bo vsak, ne vrag, le sosed bo mejak.'
#uText = u'22-letni prof. Janez je preveč "popil" (za €3.12), ko ga žena vara. Zadel je 100.000.000€ žena vara! Nato je.... '

_t2 = time.time()
result = sloTag2(uText)
_t3 = time.time()
prettyPrintWithDescription(result, dict_sl)


print "Loading time ",time.strftime("%H:%M:%S", time.gmtime(_t1-_t0)), "(",_t1-_t0,"s)"
print "Tagging time ",time.strftime("%H:%M:%S", time.gmtime(_t3-_t2)), "(",_t3-_t2,"s)"
print "Total time   ",time.strftime("%H:%M:%S", time.gmtime(_t3-_t0)), "(",_t3-_t0,"s)"
