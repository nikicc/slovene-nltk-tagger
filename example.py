# -*- coding: utf-8 -*
import nltk
import pickle
from nltk import PunktWordTokenizer
from nltk import WordPunctTokenizer

### FUNCTIONS ###
#prettPrint
def prettyPrint(uniResult):
    print ", ".join("('%s', %s)" % a for a in uniResult)

def prettyPrintByLine(uniResult):
    for a in uniResult:
        print ("('%s', %s)" % a)

#slo tag - input UNICODE
def sloTag(uText):
    tokens = WordPunctTokenizer().tokenize(uText)
    for i in tokens:
        ins = tokens.index(i)
        x = PunktWordTokenizer().tokenize(i)
        if len(x) > 1:
            tokens.remove(i)
            insX = 0
            for j in x:
                tokens.insert(ins + insX, unicode(j))
                insX +=1
    result = tagger.tag([i.encode("utf-8") for i in tokens])
    uniResult = [(unicode(i[0], "utf-8"), i[1]) for i in result]
    return uniResult
#################

#select the tagger
#tagger = pickle.load(open("slovene_taggers/TrigramTagger.pickle"))
#tagger = pickle.load(open("slovene_taggers/BrillTagger.pickle"))
tagger = pickle.load(open("slovene_taggers/NaiveBayes.pickle"))

#uText is input text
#uText = u'Lep je dan, vse diši že po pomladi!'
#uText = u'Tistega većera sem preveč popil, zgodilo se je mesec dni po tem, ko sem izvedel, da me žena vara.'
uText = u'Živé naj vsi naródi, ki hrepené dočakat dan, da, koder sonce hodi, prepir iz svéta bo pregnan, ko rojak prost bo vsak, ne vrag, le sosed bo mejak!'
result = sloTag(uText)
prettyPrintByLine(result)
