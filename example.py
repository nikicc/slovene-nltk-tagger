# -*- coding: utf-8 -*
#import nltk
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
        print ("('%s', %s)" % a)

#slo tag - input UNICODE
def sloTag(uText):
    uText = uText.encode("utf-8")
    tokens = v
    result = tagger.tag(tokens)
    uniResult = [(unicode(i[0], "utf-8"), i[1]) for i in result]
    return uniResult

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
#################

_t0 = time.time()
#select the tagger
#tagger = pickle.load(open("slovene_taggers/TrigramTagger.pickle"))
#tagger = pickle.load(open("slovene_taggers/BrillTagger.pickle"))
tagger = pickle.load(open("slovene_taggers/NaiveBayes.pickle"))
sent_tokenizer=nltk.data.load('tokenizers/punkt/slovene.pickle')
_t1 = time.time()


#uText is input text
#uText = u'Lep je dan, vse diši že po pomladi!'

#uText = u'Tistega (većera) sem-preveč "popil", zgodilo se je mesec dni po tem, ko sem izvedel, da me žena vara.'
#uText = u'Živé naj vsi naródi, ki hrepené dočakat dan, da, koder sonce hodi, prepir iz svéta bo pregnan, ko rojak prost bo vsak, ne vrag, le sosed bo mejak.'
uText = u'22-letni prof. Janez je preveč "popil" (za €3.12), ko ga žena vara. Zadel je 100.000.000€ žena vara! Nato je.... '


_t2 = time.time()
result = sloTag2(uText)
_t3 = time.time()
prettyPrintByLine(result)


print "Čas za nalaganje ",time.strftime("%H:%M:%S", time.gmtime(_t1-_t0)), "(",_t1-_t0,"s)"
print "Čas za taggganje ",time.strftime("%H:%M:%S", time.gmtime(_t3-_t2)), "(",_t3-_t2,"s)"
print "SKUPNI ČAS ",time.strftime("%H:%M:%S", time.gmtime(_t3-_t0)), "(",_t3-_t0,"s)"
