About
======
In this project we will implement NLTK Trigram Tagger for Slovene language.
##Usage
Unitl this taggers are build into NLTK, you can download the taggers from folder **slovene_taggers/** and use them in NLTK. 

The example, which shows how to use slovene taggers, is in file **example.py**

##Folders and files description
* _**trainer/**_ : the code forked from [https://github.com/japerk/nltk-trainer](https://github.com/japerk/nltk-trainer "nltk-trainer"). This trainer is used to train the Trigram tagger.

* _**jos100k/**_ : Slovene corpus taken from [JOS project](http://nl.ijs.si/jos "Slovene corpus") with 100.000 tagged words.

* _**jos1M/**_ : Slovene corpus taken from [JOS project](http://nl.ijs.si/jos "Slovene corpus") with million tagged words.

* _**pos/jos1M.pos**_ : this file is used as an input for trainer program from _trainer/_

* _**transformJOS.py**_ : the code for transforming all _.xml_ corpuses from _jos1M/_ into _jos1M.pos_.

* _**trainJOS.py**_ : the code for calling the script from _trainer/_ which trains the Tagger on _pos/jos1M.pos_ file.