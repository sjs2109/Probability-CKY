# Probability-CKY
This is an implementation of Probability CKY parsing in python. The input grammar is as same as L1 grammar, which is shown in a sample grammar file pcfg.txt, and all the grammars will be binarized if it is needed.

# I/O
The script takes two parameters:
 * The grammar file
 * The sentence to parse (which will be surrounded by double quotes)

For example:
 python prob-cky.py pcfg.txt "A test sentence ."
 
# Note
In the pre-processing part, I lemmatize some words that are not found in the grammar, so the nltk is included, which should be installed first.
 * sudo pip install -U nltk
