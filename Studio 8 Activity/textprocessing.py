## TODO1: convert allText to a single string which has all the strings appended
##		   (ex) ['I', 'am', 'healthy'] becomes "I am healthy"

## TODO2: fill in the body of the for loop here then answer to the google form question


from nltk import tokenize
import nltk

allText = [x.strip() for x in open("D:/OneDrive - 國立台灣大學/2021 2022 UCSD/Fall 2021/DSC 96/Studio 8 Activity/Course-Evaluation.csv", encoding='utf8').readlines()]

## convert allText to a single string to count word frequencies with nltk library
allText_to_string = ""
for i in range(len(allText)):
    allText_to_string = allText_to_string + " " + allText[i] ## TODO1: change the right-hand side properly

## delete the 1st space which we don't need
allText_to_string = allText_to_string[1:]

# tokenize allText and count the frequencies
wordList = tokenize.word_tokenize(allText_to_string) 
len(wordList)

# count the word frequencies and store it to a dictionary d
d = nltk.FreqDist(wordList)


# print out the word frequencies
for key in d:
    ## TODO2: fill in the body of the for loop here then answer to the google form question
    print(str(key), d[key])

print(d["seek"])
