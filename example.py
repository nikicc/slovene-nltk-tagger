# -*- coding: utf-8 -*

import nltk
import pickle
from nltk import WordPunctTokenizer
from nltk import PunktWordTokenizer
### FUNCTIONS ###
#prettPrint
def prettyPrint(uniResult):
    print ", ".join("('%s', %s)" % a for a in uniResult)

#slo tag - input UNICODE
def sloTag(uText):
    tokens = WordPunctTokenizer().tokenize(uText)
    for i in tokens:
        ins = tokens.index(i)
        x = PunktWordTokenizer().tokenize(i)
        if len(x) > 1:
            tokens.remove(i)
            alfa = 0
            for j in x:
                tokens.insert(ins + alfa,unicode(j))
                alfa +=1
    result = tagger.tag([i.encode("utf-8") for i in tokens])
    uniResult = [(unicode(i[0], "utf-8"), i[1]) for i in result]
    return uniResult
#################

#load the tagger
tagger = pickle.load(open("slovene_taggers/TrigramTagger.pickle"))

uText = u'Lep je dan, vse diši že po pomladi!'
uText = u'je s svojim obiskom v prenapolnjenih rimskih zaporih poudaril, da so razmere v rimskem zaporu slabše kot drugod v Italiji, prevelika gneča v ječi pa je "dvojna kazen", krneki.'
uText = u'Živé naj vsi naródi, ki hrepené dočakat dan, da, koder sonce hodi, prepir iz svéta bo pregnan, ko rojak prost bo vsak, ne vrag, le sosed bo mejak!'
result = sloTag(uText)
prettyPrint(result)
