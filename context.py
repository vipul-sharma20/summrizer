# coding=UTF-8
import nltk
from nltk.corpus import brown
import util


train = brown.tagged_sents(categories='news')

# backoff regex tagging
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

class ContextExtract():
    """Extracts context of the text content, relevant topics from the
       text"""

    def get_info(self, sentence):
        words = util.getWords(sentence)
        temp_tags = bigram_tag.tag(words)
        # tags = re_tag(temp_tags)


    def main():
        sentence = raw_input("sentence: ")
        get_info(sentence)
