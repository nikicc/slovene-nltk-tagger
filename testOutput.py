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
result = tagger.tag(text)

uniResult = [(unicode(pair[0],"utf-8"), pair[1]) for pair in result]

