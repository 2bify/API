import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
import re
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import warnings
warnings.filterwarnings('ignore')

from nltk.corpus import stopwords

from sklearn import preprocessing
from sklearn.feature_selection import SelectFromModel

from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.metrics import f1_score, precision_score, recall_score, precision_recall_curve, fbeta_score, confusion_matrix, accuracy_score
from sklearn.metrics import roc_auc_score, roc_curve, classification_report

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.svm import LinearSVC, SVC


from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk import ngrams, bigrams, trigrams

import pickle
import preprocess
import aiofiles

async def load_predict(text):
    # Load the vectoriser.
    # async with aiofiles.open('/home/sourjaya/MSc_Project/API_V/model_dump.pickle', mode='rb') as file:
    #     f=await file.read()
    #     model = pickle.load(f)

    # async with aiofiles.open('/home/sourjaya/MSc_Project/API_V/vectoriser.pickle', mode='rb') as file:
    #     f=await file.read()
    #     vectoriser = pickle.load(f)    
    file = open('./ML_Model/vectoriser.pickle', 'rb')
    vectoriser = pickle.load(file)
    file.close()
    # Load the SVM Model.
    file = open('./ML_Model/model_dump.pickle', 'rb')
    model = pickle.load(file)
    file.close()
    vect = vectoriser.transform(await preprocess.preprocess(text))
    sent_array = model.predict(vect)
    
    return sent_array