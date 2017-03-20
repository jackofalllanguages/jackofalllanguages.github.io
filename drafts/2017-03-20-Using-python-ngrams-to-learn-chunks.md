---
layout:single
author_profile:true
excerpt: Using python and the nltk to learn chunks
categories: linguistics tools
----


This was partly an experiment that I did to try out the [Python Natural Language ToolKit](https://www.nltk.org/), but it has some practical applications for language learning too.


# Why chunks

Learning chunks of language has various advantages. It allows us to learn phrases that we can use together without having to worry about the grammar of the particular phtase. For example in English it's must easier to learn `could have + past-participle` than to have to remember `past-tense-of-can + have + past-participle`. There are many ways that we can learn chunks. However, what if we want to start reading a book in our target language, and we'd like to know what are the most common chunks in the book? The Python NLTK comes to the rescue. Below you fill find the code for a simple Python script that will exact phrases from a data file and write them to an output file so you can study them.

# The code

```
import sys
import string
from nltk.util import ngrams
from collections import Counter

def myTokenizer(sent):
     return " ".join("".join([" " if ch in string.punctuation else ch for ch in sent]).split()).split()


def get_grams(fpath, N, max, filter=None):
    f = open(fpath, 'r')
    raw = str(f.read())
    f.close()
    token = myTokenizer(raw.decode('utf-8'))
    grams = ngrams(token,N)
    i = 0
    if not(filter is None):
        keep = [g for g in grams if filter in g]
        return Counter(keep).most_common(max)
    else:    
        return Counter(grams).most_common(max)
    
    

if __name__ == '__main__':
    args = sys.argv[1:]
    print("Usage: <fileName> <ngram-length> <number-to-print> <outfile> <optional: word-to-find>")

    out = []
    filter = None
    if len(args) > 4:
        filter = unicode(args[4])
    for x in get_grams(args[0], int(args[1]), int(args[2]), filter):
        out.insert(0,str(x[1]) + ": " + ' '.join(x[0]))
    with open(args[3], 'wR') as f:
        f.write('\n\n'.join(out).encode('utf-8'))
    print('\n')
    print(args[1]+"grams written to " + args[3])
```

# Usage

As shown at the end of the script, it take four manditory arguments and one optional one. The arguments are shown below:

1. The path to the file containing the data to analyze
2. The number of words in each phrase (the n in the ngram)
3. The number of ngrams to output
4. The output file to write the results to
5. OPTIONAL: a word that all ngrams *must* contain.

The final optional argument is useful if you want to learn how a particular word is used in the document you are studying.

## An example

We can download a text file of [The Adventures of Sherlock Holmes](http://www.gutenberg.org/cache/epub/1661/pg1661.txt) from Project Gutenberg. This text file contains license information and metadata about the recording. By removing the license info (at the end of the file) and the header info at the beginning of the file, we can get much more helpful results. The command below will find the find the 15 most common, five word phrases and save them to a file on our computer:

```
>>> python getNgrams.py pg1661.txt 5 15 results.txt
```

Then when we open of resuts.txt we will find the following results. The number on the left of the colon is the number of occurrences of the phrase tha appears to the right of the colon.

```
results.txt

4: in his chair with his

5: one to the other of

5: I do not know what

5: to the other of us

5: I shall be happy to

5: air of a man who

5: I have heard of you

5: I think that it is

5: the air of a man

5: it seemed to me that

7: from one to the other

7: I do not think that

7: in the direction of the

8: I beg that you will

13: I have no doubt that
```

