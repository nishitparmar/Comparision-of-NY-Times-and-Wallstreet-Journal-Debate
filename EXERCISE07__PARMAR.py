'''AUTHOR : NISHIT PARMAR
EXERCISE 07 
CWID : 10431431
'''
import nltk
from collections import Counter
from nltk.util import ngrams
nltk.download('punkt')
nltk.download('maxent_treebank_pos_tagger')
nltk.download('averaged_perceptron_tagger')
from nltk import bigrams
from nltk.corpus import sentiwordnet as swn

from nltk import pos_tag



demo_nyt= open ('DemocraticDebate_NYT.txt','r')
demo_wsj= open ( 'DemocraticDebate_WSJ.txt','r')
file_stopwords = open ( 'stopwords_en (1).txt' , 'r' )

NYT = []
WSJ = []
stopwords = []

for stopword in file_stopwords:
    stopwords.append( stopword.strip('\n') )
    
for text, wordlist in [(demo_nyt,NYT), (demo_wsj,WSJ)]:
    for lines in text:
        parts = lines.strip().split()
        for word in parts:
            if word.lower() not in stopwords:
                wordlist.append(word)


print '\nWSJ file without stopword: '
print
print '  '.join(NYT)
print


print '\nWSJ file without stopword: '
print
print '  '.join(WSJ)
print 

file_1 = open("DemocraticDebate_NYT.txt", 'r')
file_2 = open("DemocraticDebate_WSJ.txt",'r')	

non1= file_1.read()
non2 = file_2.read()

non1.replace('\n', ' ')
non2.replace('\n','')
words_list_NYT = []
words_list_WSJ = []
for word in non1.strip().split(): 
	words_list_NYT.append(word)

for word in non2.strip().split(): 
	words_list_WSJ.append(word)
	
top10_NYT = Counter(NYT).most_common(10)
top10_WSJ = Counter(WSJ).most_common(10)

print "The top 10 frequent NYT Words :"
for pair in top10_NYT:
    print pair[0]
    
print "The top 10 frequent WSJ Words :"
for pair in top10_WSJ:
    print pair[0]

NYT_bigram = ngrams(NYT,2)
WSJ_bigram = ngrams(WSJ,2)

NYT_big_10 = Counter(NYT_bigram).most_common(10)
WSJ_big_10 = Counter(WSJ_bigram).most_common(10)

print("\nfollowing are top 10 bigram in DemocraticDebate_NYT.txt")
for pair in NYT_big_10:
    if pair[1] <= 2:
        break
    print(pair[0][0]+" "+pair[0][1]+" : "+str(pair[1]))
print("\nfollowing are top 10 bigram in DemocraticDebate_WSJ.txt")
for pair in WSJ_big_10:
    if pair[1] <= 2:
        break
    print(pair[0][0]+" "+pair[0][1]+" : "+str(pair[1]))   
         
def senti(text):
	tagged_text = pos_tag(text)
	pos_score = neg_score = token_count = obj_score = 0
	for word, tag in tagged_text:
		try:
			ss_set = None
			if 'NN' in tag:
				ss_set = swn.senti_synset(word+'.n.01')
			elif 'VB' in tag:
				ss_set = swn.senti_synset(word+'.v.01')
			elif 'JJ' in tag:
				ss_set = swn.senti_synset(word+'.a.01')
			elif 'RB' in tag:
				ss_set = swn.senti_synset(word+ '.r.01')
			if ss_set != None:
				pos_score += ss_set.pos_score()
				neg_score += ss_set.neg_score()
				obj_score += ss_set.obj_score()
				token_count += 1
		except:
			pass
	
	return pos_score,neg_score,obj_score
print
	
print("The sentiment for NY times is : "+str(senti(WSJ)))
print("The sentiment for WSJ is : "+str(senti(NYT)))         
    


