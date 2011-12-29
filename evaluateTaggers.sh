# For evaluating the taggers after construction remove "--no-eval" argument.
# By defult this evaluate on the whole corpus.
# To evaluate tagger on only a fraction of a corpus (which is NOT used for training)
# use argument "--fraction FRACTION"

#
# EVALUATION (--fraction 0.99)
# use 99% for generating the tagger and 1% for evaluation 
# this is only used for evaluation, for real generation look above
#

mkdir tmp

date
# TrigramTagger without evaluation
python trainer/train_tagger.py --filename tmp/TrigramTagger.pickle --reader nltk.corpus.reader.tagged.TaggedCorpusReader --fileids '.+\.pos' --fraction 0.99 --default="-Neznan-" ./pos
date
# BrillTagger without evaluation
python trainer/train_tagger.py --filename tmp/BrillTagger.pickle --reader nltk.corpus.reader.tagged.TaggedCorpusReader --fileids '.+\.pos' --fraction 0.99 --default="-Neznan-" --brill ./pos
date
# ClassifierBasedPOSTagger - NaiveBayes without evaluation
python trainer/train_tagger.py --filename tmp/NaiveBayes.pickle --reader nltk.corpus.reader.tagged.TaggedCorpusReader --fileids '.+\.pos' --fraction 0.99 --default="-Neznan-" --sequential='' --classifier="NaiveBayes" ./pos
date
