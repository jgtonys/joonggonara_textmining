from konlpy.tag import Okt
from konlpy.utils import pprint
from collections import Counter
from ckonlpy.tag import Postprocessor
from ckonlpy.tag import Twitter
import codecs

from ckonlpy.utils import load_wordset

passwords = load_wordset('postprocess/passwords.txt')
stopwords = load_wordset('postprocess/stopwords.txt')

from ckonlpy.utils import load_replace_wordpair

replace = load_replace_wordpair('postprocess/replace.txt')

from ckonlpy.utils import load_ngram

ngrams = load_ngram('postprocess/ngrams.txt')

import pytagcloud

Okt = Okt()
twitter = Twitter()

new_nouns = []

with open('preprocess/dictionary.txt', encoding='utf8') as fd:
    for line in fd:
        new_nouns.append(line.strip('\n'))

twitter.add_dictionary(new_nouns, 'Noun')

passtags = {'Noun'}

postprocessor = Postprocessor(
    base_tagger=twitter,
    stopwords=stopwords,
    passtags=passtags,
    replace=replace,
    ngrams=ngrams
)

token = []
nouns = []

filename = '성동구(~2019)'

with open('outputs/서울/' + filename + '.txt', 'r') as f:
    lines = f.read()
    pre_nouns = postprocessor.pos(lines)

for w in pre_nouns:
    nouns.append(w[0])

count = Counter(nouns)

pprint(count)

f = codecs.open('wordclouds/서울/' + filename+"_wordCounting.txt", 'w', encoding='utf-8')
f.write(str(count))

tagbox = count.most_common(40)
taglist = pytagcloud.make_tags(tagbox, maxsize=80)

pytagcloud.create_tag_image(taglist, 'wordclouds/서울/' + filename + '.jpg', size=(900, 600), fontname='korean', rectangular=False)
