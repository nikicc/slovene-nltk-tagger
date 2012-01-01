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
# ./evaluateTaggers.sh 2>&1 | tee evaluation/evaluation.txt
#

mkdir tmp

#for frac in 0.99 0.98 0.97 0.96 0.95
#for frac in 0.94 0.93 0.92 0.91 0.90
for frac in 0.88 0.86 0.84 0.82 0.80 0.75
do
   echo "------------------------------------------------------------------------------------------------------------------"
   echo "-----------------------------    Fraction is $frac    -------------------------------------------------------------"                              
   echo "------------------------------------------------------------------------------------------------------------------"
   echo -n "--- TIME: "
   date
   echo "------------------------------------------------------------------------------------------------------------------"
   # TrigramTagger without evaluation
   python trainer/train_tagger.py --filename tmp/TrigramTagger.pickle --reader nltk.corpus.reader.tagged.TaggedCorpusReader --fileids '.+\.pos' --fraction  $frac --default="-Neznan-" ./pos
   echo "------------------------------------------------------------------------------------------------------------------"
   echo -n "--- TIME: "
   date
   echo "------------------------------------------------------------------------------------------------------------------"
   # BrillTagger without evaluation
   python trainer/train_tagger.py --filename tmp/BrillTagger.pickle --reader nltk.corpus.reader.tagged.TaggedCorpusReader --fileids '.+\.pos' --fraction $frac  --default="-Neznan-" --brill ./pos
   echo "------------------------------------------------------------------------------------------------------------------"
   echo -n "--- TIME: "
   date
   echo "------------------------------------------------------------------------------------------------------------------"
   # ClassifierBasedPOSTagger - NaiveBayes without evaluation
   python trainer/train_tagger.py --filename tmp/NaiveBayes.pickle --reader nltk.corpus.reader.tagged.TaggedCorpusReader --fileids '.+\.pos' --fraction $frac  --default="-Neznan-" --sequential='' --classifier="NaiveBayes" ./pos
   echo "------------------------------------------------------------------------------------------------------------------"
   echo -n "--- TIME: "
   date
done
