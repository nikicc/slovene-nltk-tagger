# For evaluating the taggers after construction remove "--no-eval" argument.
# By defult this evaluate on the whole corpus.
# To evaluate tagger on only a fraction of a corpus (which is NOT used for training)
# use argument "--fraction FRACTION"

#
# EVALUATION (--fraction 0.99)
# use 99% for generating the tagger and 1% for evaluation 
# this is only used for evaluation, for real generation look above
#
# for writing to console and file use:
# ./evaluateTaggers.sh 2>&1 | tee evaluation.log
#

mkdir tmp

for frac in 0.99 0.98 0.97 0.96 0.95
do
   echo "******************************************************************************************"
   echo "*****************************    Fraction is $frac    *************************************"                              
   echo "******************************************************************************************"
   date
   # TrigramTagger without evaluation
   python trainer/train_tagger.py --filename tmp/TrigramTagger.pickle --reader nltk.corpus.reader.tagged.TaggedCorpusReader --fileids '.+\.pos' --fraction    $frac --default="-Neznan-" ./pos
   date
   # BrillTagger without evaluation
   python trainer/train_tagger.py --filename tmp/BrillTagger.pickle --reader nltk.corpus.reader.tagged.TaggedCorpusReader --fileids '.+\.pos' --fraction $frac --default="-Neznan-" --brill ./pos
   date
   # ClassifierBasedPOSTagger - NaiveBayes without evaluation
   python trainer/train_tagger.py --filename tmp/NaiveBayes.pickle --reader nltk.corpus.reader.tagged.TaggedCorpusReader --fileids '.+\.pos' --fraction $frac --default="-Neznan-" --sequential='' --classifier="NaiveBayes" ./pos
   date
done
