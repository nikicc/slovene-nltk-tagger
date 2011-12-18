# -*- coding: utf-8 -*

import nltk
import pickle
from nltk import PunktWordTokenizer

### FUNCTIONS ###
#prettPrint
def prettyPrint(uniResult):
    print ", ".join("('%s', %s)" % a for a in uniResult)

#slo tag - input UNICODE
def sloTag(uText):
    uText = uText.encode('utf-8')
    tokens = PunktWordTokenizer().tokenize(uText)
    text = nltk.Text(tokens)
    result = tagger.tag(text)
    uniResult = [(unicode(pair[0],"utf-8"), pair[1]) for pair in result]
    return uniResult
#################

#load the tagger
tagger = pickle.load(open("slovene_taggers/TrigramTagger.pickle"))

uText = u'Lep je dan, vse diši že po pomladi!'
#uText = u'Tistega večera sem preveč popil, zgodilo se je mesec dni po tem, ko sem izvedel, da me žena vara.'
result = sloTag(uText)
prettyPrint(result)
