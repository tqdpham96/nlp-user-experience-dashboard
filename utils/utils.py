from datetime import datetime
from collections import defaultdict
import json
from collections import Counter
import numpy as np
np.random.seed(3) # for reproducibility
import pandas as pd
from heapq import nlargest
import matplotlib.pyplot as plt

# 0: neutral, 1: positive, 2: negative
def count_sentiment(data):
    pos = 0
    neg = 0
    neu = 0
    for i in data:
        try:
            if (i['nlp']['sentiment'] == 0):
                neu+=1
            elif (i['nlp']['sentiment'] == 1):
                pos+=1
            else:
                neg+=1
        except: 
            pass
    return {
        'pos': pos,
        'neg': neg,
        'neu': neu
    }

# Get data for line charting
def getSentimentTrendChartData(data):
    # Initialize a defaultdict to store counts for each sentiment
    sentiment_counts = defaultdict(lambda: {"positive": 0, "negative": 0, "neutral": 0})

    # Group the data by month
    for item in data:
        # print(item)
        try:
            published_date = datetime.fromisoformat(item["publishedAtDate"][:-1]) # Parse the date string
            month_key = f"{published_date.year}-{published_date.month:02d}"  # Create a key in the format "YYYY-MM"
            sentiment = item["nlp"]["sentiment"]

            if sentiment == 0:
                sentiment_counts[month_key]["neutral"] += 1
            elif sentiment == 1:
                sentiment_counts[month_key]["positive"] += 1
            elif sentiment == 2:
                sentiment_counts[month_key]["negative"] += 1        
        except: pass
        
    fin = list(sentiment_counts.items())
    fin.reverse()
    pos = []
    neg = []
    neu = []
    date = []
    score = []
    for i in fin:
        date.append(i[0])
        pos.append(i[1]['positive'])
        neg.append(i[1]['negative'])
        neu.append(i[1]['neutral'])
        score.append(i[1]['positive']*100/(i[1]['negative']+i[1]['positive']+i[1]['neutral']))
    
    return {
        'date': date,
        'pos': pos,
        'neg': neg,
        'neu': neu,
        'score': score,
    }

def find_top_duplicates(words, top_n=5):
    # Combine all words into a single string and split it into a list of words
    all_words = ' '.join(words).split()
    
    # Use Counter to count the occurrences of each word
    word_counts = Counter(all_words)
    
    # Find the top N duplicated words
    top_duplicates = word_counts.most_common(top_n)
    
    return top_duplicates

def getAdjFrequencyData(data):
    words = []
    for i in data:
        try:
            words.extend(i['nlp']['noun'])
        except: pass

    top_duplicates = find_top_duplicates(words)
    fWords = []
    pos = []
    neg = []
    neu = []
    for j in top_duplicates:
        fWords.append(j[0])
        _pos = 0
        _neu = 0
        _neg = 0
        for i in data:
            try:
                if (j[0] in i['nlp']['adj']) or (j[0] in i['nlp']['noun']):
                    if (i['nlp']['sentiment'] == 0):
                        _neu += 1
                    elif (i['nlp']['sentiment'] == 1):
                        _pos += 1
                    else:
                        _neg += 1
            except: pass
        
        pos.append(_pos*100/(_pos + _neu + _neg))
        neg.append(_neg*100/(_pos + _neu + _neg))
        neu.append(_neu*100/(_pos + _neu + _neg))
    

    return {
        "words": fWords,
        "pos": pos,
        "neg": neg,
        "neu": neu
    }

def getMostCommonAdj(data):
    wordPosLists = []
    wordNegLists = []
    for i in data:
        try:
            if (i['nlp']['sentiment'] == 1):
                wordPosLists.extend(i['nlp']['adj'])
            else:
                wordNegLists.extend(i['nlp']['adj'])
        except: pass

    top_duplicates_pos = find_top_duplicates(wordPosLists)
    top_duplicates_neg = find_top_duplicates(wordNegLists)


    return {
        "pos": top_duplicates_pos,
        "neg": top_duplicates_neg,
    }
    
def allTexts(data):
    nouns = []
    adjs = []
    for i in data:
        try:
            for j in i['nlp']['noun']:
                nouns.append(j)
            for j in i['nlp']['adj']:
                adjs.append(j)
        except: pass
    return nouns, adjs

def allSentences(data):
    sentencesPos = []
    sentencesNeg = []
    for i in data:
        try:
            if (i['nlp']['sentiment'] == 1):
                sentencesPos.append(i['text'])
            elif (i['nlp']['sentiment'] == 2):
                sentencesNeg.extend(i['text'])
        except: pass
    return sentencesPos, sentencesNeg

def getThreeWords(data):
    nlps=[]

    for i in data:
        try:
            if type(i['nlp']['value']) == float:
                nlps.append(i['nlp'])
        except: pass

    sorted_desc = sorted(nlps, key=lambda x: x["value"], reverse=True)
    sorted_asc = sorted(nlps, key=lambda x: x["value"], reverse=False)

    pos = []
    neg = []
    posValue = []
    negValue = []
    for i in sorted_desc:
        for j in i['long_sentence']:
            if (len(pos) == 10):
                break
            pos.append(j)
            posValue.append(i['value'])

    for i in sorted_asc:
        for j in i['long_sentence']:
            if (len(neg) == 10):
                break
            neg.append(j)
            negValue.append(abs(i['value']))

    return {
        "pos": pos,
        "posValue": posValue,
        "neg": neg,
        "negValue": negValue,
    }


def getTwoWords(data):
    nlps=[]

    for i in data:
        try:
            if type(i['nlp']['value']) == float:
                nlps.append(i['nlp'])
        except: pass

    sorted_desc = sorted(nlps, key=lambda x: x["value"], reverse=True)
    sorted_asc = sorted(nlps, key=lambda x: x["value"], reverse=False)

    pos = []
    neg = []
    posValue = []
    negValue = []
    for i in sorted_desc:
        for j in i['short_sentence']:
            if (len(pos) == 10):
                break
            pos.append(j)
            posValue.append(i['value'])

    for i in sorted_asc:
        for j in i['short_sentence']:
            if (len(neg) == 10):
                break
            neg.append(j)
            negValue.append(abs(i['value']))

    return {
        "pos": pos,
        "posValue": posValue,
        "neg": neg,
        "negValue": negValue,
    }


def co_occurrence(sentences, window_size):
    d = defaultdict(int)
    vocab = set()
    for text in sentences:
        # preprocessing (use tokenizer instead)
        text = text.lower().split()
        # iterate over sentences
        for i in range(len(text)):
            token = text[i]
            vocab.add(token)  # add to vocab
            next_token = text[i+1 : i+1+window_size]
            for t in next_token:
                key = tuple( sorted([t, token]) )
                d[key] += 1
    
    # formulate the dictionary into dataframe
    vocab = sorted(vocab) # sort vocab
    df = pd.DataFrame(data=np.zeros((len(vocab), len(vocab)), dtype=np.int16),
                      index=vocab,
                      columns=vocab)
    for key, value in d.items():
        df.at[key[0], key[1]] = value
        df.at[key[1], key[0]] = value
    return df

def build_co_occurrence_matrix(words, window_size=2, matrix_size=10):
    vocabulary = defaultdict(int)
    co_occurrence_matrix = defaultdict(lambda: defaultdict(int))

    # Build vocabulary
    for word in words:
        vocabulary[word] += 1

    # Get the most frequent words
    most_frequent_words = [word for word, _ in nlargest(matrix_size, vocabulary.items(), key=lambda x: x[1])]

    # Initialize co-occurrence matrix
    for i in most_frequent_words:
        for j in most_frequent_words:
            co_occurrence_matrix[i][j] = 0

    # Update co-occurrence matrix based on context window
    for i in range(len(words)):
        target_word = words[i]
        for j in range(max(0, i - window_size), min(len(words), i + window_size + 1)):
            if i != j:
                context_word = words[j]
                if target_word in most_frequent_words and context_word in most_frequent_words:
                    co_occurrence_matrix[target_word][context_word] += 1

    # Convert defaultdict to a regular dictionary for easier access
    co_occurrence_matrix = {k: dict(v) for k, v in co_occurrence_matrix.items()}

    return co_occurrence_matrix, most_frequent_words

def normalize_co_occurrence_matrix(co_occurrence_matrix):
    vocabulary = co_occurrence_matrix.keys()

    # Initialize the normalized co-occurrence matrix
    normalized_matrix = {i: {j: 0 for j in vocabulary} for i in vocabulary}

    # Normalize each row of the matrix
    for target_word in vocabulary:
        total_occurrences = sum(co_occurrence_matrix[target_word].values())
        for context_word in vocabulary:
            if total_occurrences > 0:
                normalized_matrix[target_word][context_word] = co_occurrence_matrix[target_word][context_word] / total_occurrences

    # Set diagonal elements to 1
    for word in vocabulary:
        normalized_matrix[word][word] = 1.0

    return normalized_matrix

def show_values(pc, fmt="%.2f", **kw):
    '''
    Heatmap with text in each cell with matplotlib's pyplot
    Source: http://stackoverflow.com/a/25074150/395857 
    By HYRY
    '''
    from itertools import izip
    pc.update_scalarmappable()
    ax = pc.get_axes()
    for p, color, value in izip(pc.get_paths(), pc.get_facecolors(), pc.get_array()):
        x, y = p.vertices[:-2, :].mean(0)
        if np.all(color[:3] > 0.5):
            color = (0.0, 0.0, 0.0)
        else:
            color = (1.0, 1.0, 1.0)
        ax.text(x, y, fmt % value, ha="center", va="center", color=color, **kw)

def cm2inch(*tupl):
    '''
    Specify figure size in centimeter in matplotlib
    Source: http://stackoverflow.com/a/22787457/395857
    By gns-ank
    '''
    inch = 2.54
    if type(tupl[0]) == tuple:
        return tuple(i/inch for i in tupl[0])
    else:
        return tuple(i/inch for i in tupl)

def heatmap(AUC, title, xlabel, ylabel, xticklabels, yticklabels):
    '''
    Inspired by:
    - http://stackoverflow.com/a/16124677/395857 
    - http://stackoverflow.com/a/25074150/395857
    '''

    # Plot it out
    fig, ax = plt.subplots()    
    c = ax.pcolor(AUC, edgecolors='k', linestyle= 'dashed', linewidths=0.2, cmap='RdBu', vmin=0.0, vmax=1.0)

    # put the major ticks at the middle of each cell
    ax.set_yticks(np.arange(AUC.shape[0]) + 0.5, minor=False)
    ax.set_xticks(np.arange(AUC.shape[1]) + 0.5, minor=False)

    # set tick labels
    #ax.set_xticklabels(np.arange(1,AUC.shape[1]+1), minor=False)
    ax.set_xticklabels(xticklabels, minor=False)
    ax.set_yticklabels(yticklabels, minor=False)

    # set title and x/y labels
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)      

    # Remove last blank column
    plt.xlim( (0, AUC.shape[1]) )

    # Turn off all the ticks
    ax = plt.gca()    
    for t in ax.xaxis.get_major_ticks():
        t.tick1On = False
        t.tick2On = False
    for t in ax.yaxis.get_major_ticks():
        t.tick1On = False
        t.tick2On = False

    # Add color bar
    plt.colorbar(c)

    # Add text in each cell 
    show_values(c)

    # Proper orientation (origin at the top left instead of bottom left)
    ax.invert_yaxis()
    ax.xaxis.tick_top()

    # resize 
    fig = plt.gcf()
    fig.set_size_inches(cm2inch(40, 20))
    return fig


def process_co_occurrence_matrix(data):
    sentencesN, sentencesA = allTexts(data)
    sentencesN.extend(sentencesA)
    fi = []
    for i in sentencesN:
        fi.append(i.lower())
    co_occurrence_matrix, vocabulary = build_co_occurrence_matrix(fi)
    normalized_matrix = normalize_co_occurrence_matrix(co_occurrence_matrix)
    f_normalized_matrix = np.array([[normalized_matrix[i][j] for j in normalized_matrix[i]] for i in normalized_matrix])
    return f_normalized_matrix, vocabulary

def getEmotionAspect(data):
    supportedEmotion = ["Happy", "Angry", "Sad", "Surprise", "Fear"]
    nouns = []
    for i in data:
        try:
            for j in i['nlp']['noun']:
                nouns.append(j.lower())
        except: pass
    nounsUnique = find_top_duplicates(nouns, top_n=10)
    fin = {}
    x = []
    for i in nounsUnique:
        x.append(i[0])
        fin[i[0]] = {"Happy": [], "Angry": [],"Sad": [],"Surprise": [],"Fear": []}
        for j in data:
            try:
                if i[0] in j['nlp']['noun']:
                    fin[i[0]][j['nlp']['emotion']].append(abs(j['nlp']['value']))
            except: pass

    matrix = []
    for i in supportedEmotion:
        row = []
        for j in nounsUnique:
            m = np.average(fin[j[0]][i])
            if m>0:
                row.append(m)
            else:
                row.append(np.random.uniform(0.01, 0.03))
            pass
        matrix.append(row)
    return matrix, x, supportedEmotion

def getMostSentences(data):
    dicSentence = {}
    dicUserName = {}
    dicUserNoReview = {}
    dicUserAvatar = {}
    dicUserLink = {}
    dicUserLikedCount = {}
    dicUserStar = {}
    dicUserPublishedAt = {}

    pos = []
    neg = []
    for i in data:
        try:
            if (i['nlp']['sentiment'] == 1):
                pos.append(i['nlp']['value'])
                dicSentence[i['nlp']['value']] = i['text']
                dicUserName[i['nlp']['value']] = i['name']
                dicUserNoReview[i['nlp']['value']] = i['noReview']
                dicUserAvatar[i['nlp']['value']] = i['reviewerPhotoUrl']
                dicUserLink[i['nlp']['value']] = i['reviewerUrl']
                dicUserLikedCount[i['nlp']['value']] = i['likesCount']
                dicUserStar[i['nlp']['value']] = i['stars']
                dicUserPublishedAt[i['nlp']['value']] = i['publishedAtDate']

            elif (i['nlp']['sentiment'] == 2):
                neg.append(i['nlp']['value'])
                dicSentence[i['nlp']['value']] = i['text']
                dicUserName[i['nlp']['value']] = i['name']
                dicUserNoReview[i['nlp']['value']] = i['noReview']
                dicUserAvatar[i['nlp']['value']] = i['reviewerPhotoUrl']
                dicUserLink[i['nlp']['value']] = i['reviewerUrl']
                dicUserLikedCount[i['nlp']['value']] = i['likesCount']
                dicUserStar[i['nlp']['value']] = i['stars']
                dicUserPublishedAt[i['nlp']['value']] = i['publishedAtDate']

        except: pass
    pos.sort(reverse=True)
    neg.sort()
    
    final = {'pos': {'sentence': [], 'name': [],'noReview': [],'avatar': [],'link': [],'likedCount': [],'star': [],'time': []}, 'neg':{'sentence': [], 'name': [],'noReview': [],'avatar': [],'link': [],'likedCount': [],'star': [],'time': []}}
    for i in pos[0:10]:
        try:
            final['pos']['sentence'].append(dicSentence[i])
            final['pos']['name'].append(dicUserName[i])
            final['pos']['noReview'].append(dicUserNoReview[i])
            final['pos']['avatar'].append(dicUserAvatar[i])
            final['pos']['link'].append(dicUserLink[i])
            final['pos']['likedCount'].append(dicUserLikedCount[i])
            final['pos']['star'].append(dicUserStar[i])
            final['pos']['time'].append(dicUserPublishedAt[i])
        except: pass
    for i in neg[0:10]:
        try:
            final['neg']['sentence'].append(dicSentence[i])
            final['neg']['name'].append(dicUserName[i])
            final['neg']['noReview'].append(dicUserNoReview[i])
            final['neg']['avatar'].append(dicUserAvatar[i])
            final['neg']['link'].append(dicUserLink[i])
            final['neg']['likedCount'].append(dicUserLikedCount[i])
            final['neg']['star'].append(dicUserStar[i])
            final['neg']['time'].append(dicUserPublishedAt[i])
        except: pass
    return final

    
