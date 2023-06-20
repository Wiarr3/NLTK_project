from .models import Text
from textblob import TextBlob
import nltk

nltk.download('brown')
nltk.download('punkt')


def get_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return round(sentiment,2)


def get_word_count(text):
    words = text.split()
    word_count = len(words)
    return word_count


def get_keywords(text):
    blob = TextBlob(text)
    keywords = blob.noun_phrases
    print(keywords)
    return ' '.join(keywords)


def count_words_by_tag(text, tag):
    blob = TextBlob(text)
    words = blob.tags
    count = 0
    for word, word_tag in words:
        if word_tag == tag:
            count += 1
    return count


def get_tags(text):
    blob = TextBlob(text)
    tags = [tag for word, tag in blob.tags]
    result_dict = {}
    for tag in tags:
        count = count_words_by_tag(text, tag)
        result_dict[tag] = count

    result = [(count, tag) for tag, count in result_dict.items()]
    s = ''
    for x in result:
        s += f'{x[1]}: {x[0]} \n'
    print(s)
    return s


def process_whole(raw_text, userId):
    sentiment = get_sentiment(raw_text)
    word_count = get_word_count(raw_text)
    keywords = get_keywords(raw_text)
    tags = get_tags(raw_text)

    return Text(rawText=raw_text, sentiment=sentiment, wordCount=word_count, keywords=keywords, tags=tags,
                user_id=userId)


def get_start_of_text(text):
    if len(text) <= 6:
        return text + '...'
    else:
        words = text.split(' ')
        result = ""
        count = 0
        for word in words:
            if count + len(word) <= 60:
                result += word + " "
                count += len(word) + 1
            else:
                break
        return result.strip() + '...'
