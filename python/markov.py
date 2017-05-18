#!/usr/bin/env python

# Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

# ```bash
# ./markov.py chains.txt 40
# ```

# A possible output would be:

# > show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

# There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.

import sys
import re
import random

def main(argv):
    filename = ''
    nWords = 0
    try:
        filename = argv[0]
        nWords = int(argv[1])
        f = open(filename, 'r')
    except:
        print("markov.py <filename> <number of words>")
        sys.exit(2)
    markov = buildDict(f)

    sentence = ''
    i = 0
    word = random.choice(list(markov.keys()))
    while i < nWords and word != '':
        sentence += word + ' '
        i += 1
        word = nextWord(word, markov)
    print(sentence)

#builds a dictionary that can be used to generate next words based on the current one
def buildDict(f):
    #read and parse text
    data = f.read()
    data = re.sub('\n', ' ', data)
    words = re.split('[ @.,]',data)
    words = list(filter(None, words))
    #build a dictionary detailing the frequencies of words following specific words
    markovDict = {}
    for i in range(len(words)-1):
        if words[i] not in markovDict:
            markovDict[words[i]] = {}
        if words[i+1] not in markovDict[words[i]]:
            markovDict[words[i]][words[i+1]] = 0
        markovDict[words[i]][words[i+1]] += 1
    #end if we're at a stopword
    if words[len(words)-1] not in markovDict:
        markovDict[words[len(words)-1]] = {'': 1}
    return markovDict

#use the dictionary to generate the next word
def nextWord(word, markov):
    candidates = markov[word]
    #weight the choices weighted by the number of occurrences
    return random.choice([k for k in candidates for dummy in range(candidates[k])])

if __name__ == '__main__':
    main(sys.argv[1:])
