# coding=UTF-8
import nltk
from nltk.corpus import brown

train = brown.tagged_sents(categories='news')
regex_tag = nltk.RegexpTagger([
     (r'^[-\:]?[0-9]+(.[0-9]+)?$', 'CD'),
     (r'.*able$', 'JJ'),
     (r'^[A-Z].*$', 'NNP'),
     (r'.*ly$', 'RB'),
     (r'.*s$', 'NNS'),
     (r'.*ing$', 'VBG'),
     (r'.*ed$', 'VBD'),
     (r'.*', 'NN')
])


unigram_tag = nltk.UnigramTagger(train, backoff=regex_tag)
bigram_tag = nltk.BigramTagger(train, backoff=unigram_tag)


def get_words(sentence):
    words = nltk.word_tokenize(sentence)
    return words


def get_info(sentence):
    words = get_words(sentence)
    tags = bigram_tag.tag(words)


def main():
    sentence = raw_input("sentence: ")
    get_info(sentence)

main()
