#
# for writing to console and file use:
# python evaluateTaggersSpeed.py 2>&1 | tee evaluation/evaluation_speed.txt
#

import pickle
import time
import sys

f = open( "pos/jos1M.pos", "r" )
words = []
for line in f.readlines():
    for t in line.split():
        words.append(t.split('/')[0])
print "We have ",len(words)," words."
sys.stdout.flush()

_t0 = time.time()
taggerBrillTagger = pickle.load( open("slovene_taggers/BrillTagger.pickle") )
taggerTrigramTagger = pickle.load( open("slovene_taggers/TrigramTagger.pickle") )
taggerNaiveBayes = pickle.load( open("slovene_taggers/NaiveBayes.pickle") )
_t1 = time.time()
print "All taggers loaded in: ",time.strftime("%H:%M:%S", time.gmtime(_t1-_t0)), "(",_t1-_t0,"s )"
sys.stdout.flush()

timeBrillTagger = []
timeTrigramTagger = []
timeNaiveBayes = []
nWords = [50,75,100,125,150,175,200,225,250,275,300,325,350,400,425,450,475,500]
for l in nWords:
    _t2 = time.time()
    taggerBrillTagger.tag(words[:l])
    _t3 = time.time()
    taggerTrigramTagger.tag(words[:l])
    _t4 = time.time()
    taggerNaiveBayes.tag(words[:l])
    _t5 = time.time()
    print "NUMBER OF WORDS: ",l
    print "taggerBrillTagger   ",_t3-_t2, "s"
    sys.stdout.flush()
    timeBrillTagger.append(_t3-_t2)
    print "taggerTrigramTagger ",_t4-_t3, "s"
    sys.stdout.flush()
    timeTrigramTagger.append(_t4-_t3)
    print "taggerNaiveBayes    ",_t5-_t4, "s"
    sys.stdout.flush()
    timeNaiveBayes.append(_t5-_t4)
    
print "nWords =",nWords
print "timeBrillTagger =",timeBrillTagger
print "timeTrigramTagger =",timeTrigramTagger
print "timeNaiveBayes =",timeNaiveBayes
