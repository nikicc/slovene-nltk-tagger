# -*- coding: utf-8 -*
#MUltext-east
from nltk import PunktWordTokenizer

import nltk

import pickle
tagger = pickle.load(open("C:/users/banic/nltk_data/taggers/_aubt.pickle"))

#unicode_text = u'Lep je dan, vse diši že po pomladi'
unicode_text = u'Tistega večera sem preveč popil, zgodilo se je mesec dni po tem, ko sem izvedel, da me žena vara .'
unicode_text = unicode_text.encode('utf-8')
tokens = PunktWordTokenizer().tokenize(unicode_text)
text = nltk.Text(tokens)
L= tagger.tag(text)
#REZULTAT = [('Tistega', 'PPNMER'), ('ve\xc4\x8dera', 'SOMER'), ('sem', 'GP-SPE-N'), ('preve\xc4\x8d', 'RSN'), ('popil', 'GGDD-EM'), (',', ','), ('zgodilo', 'GGDD-ES'), ('se', 'ZP------K'), ('je', 'GP-STE-N'), ('mesec', 'SOMETN'), ('dni', 'SOMMR'), ('po', 'DM'), ('tem', 'ZK-MEM'), (',', ','), ('ko', 'VD'), ('sem', 'GP-SPE-N'), ('izvedel', 'GGDD-EM'), (',', ','), ('da', 'VD'), ('me', 'ZOP-ET--K'), ('\xc5\xbeena', 'SOZEI'), ('vara', 'PPNZEI'), ('.', '.')]
#print REZULTAT

#b = [()]
b = [(i[0].decode("utf-8").encode('cp1250'),i[1]) for i in L]
for i in b:
    print "("+i[0]+" : "+i[1]+")"