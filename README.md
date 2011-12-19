About
======
In this project we will implement NLTK Taggers for Slovene language.

##Reqirements

For this tagger to work, you need Python 2.7 and NLTK.

##Usage

Unitl this taggers are build into NLTK, you can download the taggers from folder **slovene_taggers/** and use them in NLTK. 

The example, which shows how to use Slovene taggers, is in file **example.py**

Slovenian explanation of tags is in **jos1M/josMSD-canon-sl.tbl**

##Folders and files description

* _**jos100k/**_ : Slovene corpus taken from [JOS project](http://nl.ijs.si/jos "Slovene corpus") with 100.000 tagged words.

* _**jos1M/**_ : Slovene corpus taken from [JOS project](http://nl.ijs.si/jos "Slovene corpus") with million tagged words.

* _**pos/jos1M.pos**_ : this file is used as an input for trainer program from _trainer/_

* _**slovene_taggers/**_ : the result of this project. Here are strored Slovene Taggers, which can be used in NLTK.

* _**trainer/**_ : the code forked from [https://github.com/japerk/nltk-trainer](https://github.com/japerk/nltk-trainer "nltk-trainer"). This trainer is used to train the taggers.

* _**example.py**_ : this example shows, how to use Slovene taggers in NLTK.

* _**generateTaggers.sh**_ : commands for generating the taggers. The generation uses data _pos/jos1M.pos_ and program _trainer/train_tagger.py_. 

* _**transformJOS.py**_ : the code for transforming all _.xml_ corpuses from _jos1M/_ into _pos/jos1M.pos_.