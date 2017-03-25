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