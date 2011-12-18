# -*- coding: utf-8 -*
import nltk
import pickle
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
    uText = uText.encode('utf-8')
    tokens = PunktWordTokenizer().tokenize(uText)
    text = nltk.Text(tokens)
    result = tagger.tag(text)
    uniResult = [(unicode(pair[0],"utf-8"), pair[1]) for pair in result]
    return uniResult
#################

#select the tagger
#tagger = pickle.load(open("slovene_taggers/TrigramTagger.pickle"))
#tagger = pickle.load(open("slovene_taggers/BrillTagger.pickle"))
tagger = pickle.load(open("slovene_taggers/NaiveBayes.pickle"))

#uText is input text
#uText = u'Lep je dan, vse diši že po pomladi!'
#uText = u'Tistega večera sem preveč popil, zgodilo se je mesec dni po tem, ko sem izvedel, da me žena vara.'
uText = u'Živé naj vsi naródi, ki hrepené dočakat dan, da, koder sonce hodi, prepir iz svéta bo pregnan, ko rojak prost bo vsak, ne vrag, le sosed bo mejak!'
result = sloTag(uText)
prettyPrintByLine(result)
