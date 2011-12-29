#
# GENERATION
#

mkdir slovene_taggers

date
# TrigramTagger without evaluation
python trainer/train_tagger.py --filename slovene_taggers/TrigramTagger.pickle --reader nltk.corpus.reader.tagged.TaggedCorpusReader --fileids '.+\.pos' --default="-Neznan-" --no-eval ./pos
date
# BrillTagger without evaluation
python trainer/train_tagger.py --filename slovene_taggers/BrillTagger.pickle --reader nltk.corpus.reader.tagged.TaggedCorpusReader --fileids '.+\.pos' --default="-Neznan-" --brill --no-eval ./pos
date
# ClassifierBasedPOSTagger - NaiveBayes without evaluation
python trainer/train_tagger.py --filename slovene_taggers/NaiveBayes.pickle --reader nltk.corpus.reader.tagged.TaggedCorpusReader --fileids '.+\.pos' --default="-Neznan-" --sequential='' --classifier="NaiveBayes" --no-eval ./pos
date
