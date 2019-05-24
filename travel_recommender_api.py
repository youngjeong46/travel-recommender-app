import os
import json
import pickle
import numpy as np
import pandas as pd
import re

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF

vectorizer = pickle.load(open("models/tfidf.pickle", "rb"))
model = pickle.load(open("models/nmf.pickle", "rb"))
results = pickle.load(open("models/results.pickle", "rb"))
pos = pickle.load(open("models/reviews.pickle", "rb"))


def punctuations(text):
    text = re.sub(r"[^a-z0-9(),!.?\'`]", " ", text)
    text = re.sub(r"\'s", "", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r"[(),!.?\'`]", "", text)
    text = re.sub(r"\s{2,}", " ", text)
    text = re.sub(r"\s[a-z]{1,2}\s", " ", text)
    return text


def clean_single(row):
    row = row.strip().lower()
    return punctuations(row)


def suggest(description):
    # Preprocessing
    description = clean_single(description)

    # Tokenize, Vectorize and Tranform using model
    user_matrix = vectorizer.transform([description])
    user_topic = model.transform(user_matrix)

    cosines = cosine_similarity(user_topic, results)

    # Find max cosine similarity and print the original review content
    idx = cosines[0].argsort()[-3:][::-1]

    suggestions = {

    }
    for i in range(len(idx)):
        suggestions[str(i)] = {'hotel': pos.iloc[idx[i], :].hotel,
                               'city': pos.iloc[idx[i], :].city,
                               'review': pos.iloc[idx[i], :].content}

    print(suggestions)

    return suggestions


if __name__ == '__main__':
    print(suggest("I want to go ski."))
