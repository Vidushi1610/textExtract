import re
import syllapy
import nltk 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob


pronounRegex = re.compile(r'I|we|my|ours|us',re.I)
file = open("test.txt", "rt")
data = file.read()
words = data.split()
total = sum(map(len, words))/len(words)
parts = [len(l.split()) for l in re.split(r'[?!.]', data) if l.strip()]
pronouns = pronounRegex.findall(data)
res = TextBlob(data)
#s= syllapy.count("data")
sid = SentimentIntensityAnalyzer()
ss = sid.polarity_scores(data)

#-----------------------------------------------------------------------------#
print('2.  POSITIVE SCORE', ss['pos']*100)
print('3.  NEGAVTIVE SCORE', ss['neg']*100)
print('4.  POLARITY SCORE', res.sentiment.polarity*100)
print('9.  AVG NUMBER OF WORDS PER SENTENCE', sum(parts)/len(parts))
#print('10. COMPLEX WORD COUNT',(complex))
print('11. WORD COUNT:', len(words))
#print('12. SYLLABLE PER WORD:', (s))
print('13. PERSONAL PRONOUNS',len(pronouns))
print('14. AVG WORD LENGTH', (total))



