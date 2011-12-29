# For evaluating the taggers after construction remove "--no-eval" argument.
# By defult this evaluate on the whole corpus.
# To evaluate tagger on only a fraction of a corpus (which is NOT used for training)
# use argument "--fraction FRACTION"

#
# GENERATION
#

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

#
# EVALUATION (--fraction 0.99)
# use 99% for generating the tagger and 1% for evaluation 
# this is only used for evaluation, for real generation look above
#

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
