import nltk
nltk.download('stopwords')
nltk.download('wordnet')
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import warnings
warnings.filterwarnings('ignore')
import re
# Defining dictionary containing all emojis with their meanings.
emojis = {':)': 'smile', ':-)': 'smile', ';d': 'wink', ':-E': 'vampire', ':(': 'sad', 
          ':-(': 'sad', ':-<': 'sad', ':P': 'raspberry', ':O': 'surprised',
          ':-@': 'shocked', ':@': 'shocked',':-$': 'confused', ':\\': 'annoyed', 
          ':#': 'mute', ':X': 'mute', ':^)': 'smile', ':-&': 'confused', '$_$': 'greedy',
          '@@': 'eyeroll', ':-!': 'confused', ':-D': 'smile', ':-0': 'yell', 'O.o': 'confused',
          '<(-_-)>': 'robot', 'd[-_-]b': 'dj', ":'-)": 'sadsmile', ';)': 'wink', 
          ';-)': 'wink', 'O:-)': 'angel','O*-)': 'angel','(:-D': 'gossip', '=^.^=': 'cat'}

## Defining set containing all stopwords in english.
stopwordlist = ['a', 'about', 'above', 'after', 'again', 'ain', 'all', 'am', 'an',
             'and','any','are', 'as', 'at', 'be', 'because', 'been', 'before',
             'being', 'below', 'between','both', 'by', 'can', 'd', 'did', 'do',
             'does', 'doing', 'down', 'during', 'each','few', 'for', 'from', 
             'further', 'had', 'has', 'have', 'having', 'he', 'her', 'here',
             'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in',
             'into','is', 'it', 'its', 'itself', 'just', 'll', 'm', 'ma',
             'me', 'more', 'most','my', 'myself', 'now', 'o', 'of', 'on', 'once',
             'only', 'or', 'other', 'our', 'ours','ourselves', 'out', 'own', 're',
             's', 'same', 'she', "shes", 'should', "shouldve",'so', 'some', 'such',
             't', 'than', 'that', "thatll", 'the', 'their', 'theirs', 'them',
             'themselves', 'then', 'there', 'these', 'they', 'this', 'those', 
             'through', 'to', 'too','under', 'until', 'up', 've', 'very', 'was',
             'we', 'were', 'what', 'when', 'where','which','while', 'who', 'whom',
             'why', 'will', 'with', 'won', 'y', 'you', "youd","youll", "youre",
             "youve", 'your', 'yours', 'yourself', 'yourselves']


# Function for text preprocessing
async def preprocess(tweets):
    processed_tweet = []
    
    # Creating Lemmatizer and Stemmer.
    wordLemm = WordNetLemmatizer()
    
    # Defining regex patterns.
    username_remove       = '@[^\s]+'
    #The regular expression ((http://)[^ ]*|(https://)[^ ]*|(www\.)[^ ]*) 
    #matches any string that starts with "http://", "https://", or "www.", followed by any number of non-space characters
    url_remove        = r"((http://)[^ ]*|(https://)[^ ]*|( www\.)[^ ]*)"

    #The regular expression [^a-zA-Z0-9] matches any single character that is not a letter (uppercase or lowercase) or a digit.
    non_alpha      = "[^a-zA-Z0-9]"

    #The regular expression (.)\1\1+ matches any sequence of three or more consecutive identical characters.
    pattern   = r"(.)\1\1+"

    #The regular expression \1\1 is a backreference that matches any two consecutive identical characters.
    replace_pattern = r"\1\1"

    #The regular expression \w*\d\w* matches any string that contains at least one digit (\d) 
    #and zero or more word characters (\w) before and after the digit.
    #alphanumeric = '\w*\d\w*'

    #creates a regular expression pattern that matches any single character that is 
    #a member of the punctuation character set defined in the Python string module.
    punc_lower = '[%s]' % re.escape(string.punctuation)

    #The regular expression "\n" matches a newline character in a string.
    remove_n = "\n"

    #The regular expression [^\x00-\x7f] matches any single character that is not a standard ASCII character.
    remove_non_ascii = r'[^\x00-\x7f]'
    
    for tweet in tweets:
        tweet = tweet.lower()
        
        # Replacing all URls with 'URL'
        tweet = re.sub(url_remove,' URL',tweet)

        # Replacing all emojis.
        for emoji in emojis.keys():
            tweet = tweet.replace(emoji, "EMOJI" + emojis[emoji])

        # Replacing @USERNAME to 'USER'.
        tweet = re.sub(username_remove,' USER', tweet)

        # Replacing all non alphabets.
        tweet = re.sub(non_alpha, " ", tweet)


        # Replacing alphanumeric
        #tweet = re.sub('\w*\d\w*', ' ', tweet)

        # Replacing punctuation
        tweet = re.sub(punc_lower, ' ', tweet)

        # Replacing \n
        tweet = re.sub(remove_n, " ", tweet)

        # Replacing non-ascii
        tweet = re.sub(remove_non_ascii, r' ', tweet)

        # Replacing 3 or more consecutive letters by 2 letters.
        tweet = re.sub(pattern, replace_pattern, tweet)

        new_tweet = ''
        for word in tweet.split():
            if word not in stopwordlist or len(word) > 1:
                word = wordLemm.lemmatize(word)
                new_tweet += (word+' ')
            
        processed_tweet.append(new_tweet)
        
    return processed_tweet