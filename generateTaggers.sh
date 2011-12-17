# For evaluating the taggers after construction remove "--no-eval" argument.
# By defult this evaluate on the whole corpus, which might take a lot of time.
# To evaluate tagger on only a fraction of a corpus use argument "--fraction FRACTION"

# TrigramTagger without evaluation
python trainer/train_tagger.py --filename slovene_taggers/TrigramTagger.pickle --reader nltk.corpus.reader.tagged.TaggedCorpusReader --fileids '.+\.pos' --default="-Neznan-" --no-eval ./pos

# BrillTagger without evaluation
python trainer/train_tagger.py --filename slovene_taggers/BrillTagger.pickle --reader nltk.corpus.reader.tagged.TaggedCorpusReader --fileids '.+\.pos' --default="-Neznan-" --brill --no-eval ./pos

# ClassifierBasedPOSTagger - NaiveBayes without evaluation
python trainer/train_tagger.py --filename slovene_taggers/NaiveBayes.pickle --reader nltk.corpus.reader.tagged.TaggedCorpusReader --fileids '.+\.pos' --default="-Neznan-" --sequential='' --classifier="NaiveBayes" --no-eval ./pos

# ClassifierBasedPOSTagger - Maxent without evaluation
python trainer/train_tagger.py --filename slovene_taggers/Maxent.pickle --reader nltk.corpus.reader.tagged.TaggedCorpusReader --fileids '.+\.pos' --default="-Neznan-" --sequential='' --classifier="Maxent" --no-eval ./pos

# ClassifierBasedPOSTagger - NaiveBayes, Maxent without evaluation
python trainer/train_tagger.py --filename slovene_taggers/NaiveBayesMaxent.pickle --reader nltk.corpus.reader.tagged.TaggedCorpusReader --fileids '.+\.pos' --default="-Neznan-" --sequential='' --classifier=["NaiveBayes","Maxent"] --no-eval ./pos

# ClassifierBasedPOSTagger - DecisionTree without evaluation
python trainer/train_tagger.py --filename slovene_taggers/DecisionTree.pickle --reader nltk.corpus.reader.tagged.TaggedCorpusReader --fileids '.+\.pos' --default="-Neznan-" --sequential='' --classifier="DecisionTree" --no-eval ./pos


#
# WITH EVALUATION (--fraction 0.01)
#

# TrigramTagger without evaluation
#python trainer/train_tagger.py --filename slovene_taggers/TrigramTagger.pickle --reader nltk.corpus.reader.tagged.TaggedCorpusReader --fileids '.+\.pos' --fraction 0.01 --default="-Neznan-" ./pos

# BrillTagger without evaluation
#python trainer/train_tagger.py --filename slovene_taggers/BrillTagger.pickle --reader nltk.corpus.reader.tagged.TaggedCorpusReader --fileids '.+\.pos' --fraction 0.01 --default="-Neznan-" --brill ./pos

# ClassifierBasedPOSTagger - NaiveBayes without evaluation
#python trainer/train_tagger.py --filename slovene_taggers/NaiveBayes.pickle --reader nltk.corpus.reader.tagged.TaggedCorpusReader --fileids '.+\.pos' --fraction 0.01 --default="-Neznan-" --sequential='' --classifier="NaiveBayes" ./pos

# ClassifierBasedPOSTagger - Maxent without evaluation
#python trainer/train_tagger.py --filename slovene_taggers/Maxent.pickle --reader nltk.corpus.reader.tagged.TaggedCorpusReader --fileids '.+\.pos' --fraction 0.01 --default="-Neznan-" --sequential='' --classifier="Maxent" ./pos

# ClassifierBasedPOSTagger - NaiveBayes, Maxent without evaluation
#python trainer/train_tagger.py --filename slovene_taggers/NaiveBayesMaxent.pickle --reader nltk.corpus.reader.tagged.TaggedCorpusReader --fileids '.+\.pos' --fraction 0.01 --default="-Neznan-" --sequential='' --classifier=["NaiveBayes","Maxent"] ./pos

# ClassifierBasedPOSTagger - DecisionTree without evaluation
#python trainer/train_tagger.py --filename slovene_taggers/DecisionTree.pickle --reader nltk.corpus.reader.tagged.TaggedCorpusReader --fileids '.+\.pos' --fraction 0.01 --default="-Neznan-" --sequential='' --classifier="DecisionTree" ./pos
