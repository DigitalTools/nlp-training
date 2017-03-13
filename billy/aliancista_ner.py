from __future__ import division
import nltk
from nltk.probability import FreqDist
import io

f = io.open('aliancista.txt', 'rU', encoding='utf-8')
raw = f.read()
tokens = nltk.word_tokenize(raw)

#print 'tokens: ', len(tokens)

def get_meaninful_content(text):
  stopwords = nltk.corpus.stopwords.words('spanish')
  #content = [w for w in text if w.lower() not in stopwords]
  content = [w for w in text if w.lower() not in stopwords and len(w)>1]
  return content

content = get_meaninful_content(tokens)

def content_fraction(text, content):
  return len(content) / len(text)

text = nltk.Text(content)

fdist = FreqDist(content)

#vocab = fdist.keys()
#print vocab[:25]

#fdist.plot(50, cumulative=True)

#mostFreqW = sorted([w for w in set(text) if fdist[w]>6])

#for w in mostFreqW:
#  print w.encode('utf-8') , ': ' , fdist[w]

mostFreqWDist = fdist.most_common(5)
#print mostFreqWDist
#for t in mostFreqWDist:
#  print t[0].encode('utf-8'), ':', t[1]

mostFreqW = [ t[0] for t in mostFreqWDist ]

def get_full_text(text):
  #content = [w for w in text if w.lower() not in stopwords]
  full_content = [w for w in text]
  full_text = nltk.Text(full_content)
  return full_text

full_text = get_full_text(tokens)

#full_text.concordance(u'pap\xe1')

#full_text.dispersion_plot(mostFreqW)

#for w in tokens:
#  if w.startswith(u'\xe9st'):
#    print w.encode('utf-8')

#full_text.concordance(u'\xe9ste')
#full_text.concordance(u'\xe9l')
#full_text.concordance('esposo')



