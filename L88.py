__author__ = 'Hernan Y.Ke'
#map and reduce
from functools import reduce

doc = ['Comprehensions are simple, but powerful',
       'syntaxes that allow us to transform or filter an iterable object in as little as one line of code. The resultant object can be a perfectly normal list, set, or dictionary, or it can be a',
       'generator expression that can be efficiently consumed in one go']

def count_words(doc):
    normalized_doc = ''.join(c.lower() if c.isalpha() else ' 'for c in doc) # convert all non-char to blank
    freq = {}
    for word in normalized_doc.split(' '):
        freq[word]=freq.get(word,0)+1  #Second arg 0 is default value
    return freq

counts = map(count_words,doc)


def combine_counts(d1,d2):
    d = d1.copy()
    for word, count in d2.items():
        d[word] = d.get(word,0)+count
    return d

total_counts = reduce(combine_counts,counts)
print(total_counts)