## TODO1: calculate the average of each scores (neutral, negative, positive, and compound)

from nltk import tokenize
import nltk
import babypandas as bpd

from nltk.sentiment.vader import SentimentIntensityAnalyzer

allText = [x.strip() for x in open("Course-Evaluation.csv", encoding='utf8').readlines()]

# sentiment analysis results are stored in a list named csSentimentals
ceSentiments = []

# initialize a sentiment analysis module, named as analyzer
analyzer = SentimentIntensityAnalyzer()


# store sentiment analysis results for each student response
# ceSentiments is a list of dictionaries, with the actual responses and sentiments
# sentiments are represented with 4 types of scores: neutral, negative, positive, and compound
for response in allText:
    ceSentiment = analyzer.polarity_scores(response)
    ceSentiment['text'] = response
    ceSentiments.append(ceSentiment)
    


## TODO1: calculate the average of each scores
total = bpd.DataFrame.from_dict(ceSentiments)
print(total.columns)

neu_avg = total.get('neu').sum()/total.shape[0]
neg_avg = total.get('neg').sum()/total.shape[0]
pos_avg = total.get('pos').sum()/total.shape[0]
com_avg = total.get('compound').sum()/total.shape[0]
print(neu_avg, neg_avg, pos_avg, com_avg)