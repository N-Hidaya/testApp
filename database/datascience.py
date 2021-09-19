# has 1 parameter, a Series, representing each row of the dataframe
# extracts all the required values from said row using .at[]
# does the data processing using basic python operations: .split, list comprehension, etc.
# returns the data either as a joined string or as a list of words, as the problem requires
#and then use .apply(..., axis=1) to apply the function to every row of the dataframe
#i'll give you the answer i would personally use, trusting that you won't blindly copy and paste:

import sqlite3
from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('tweets.sqlite')

tweets_cursor = db.execute('''
SELECT e.tweet_id, t.full_text, e.value, e.start_index, e.end_index
FROM Entities e
  JOIN Tweets t ON t.id = e.tweet_id
''')

# If you wanted to get the column names from the db; optional
#tweets_colnames = [desc[0] for desc in tweets_cursor.description]
tweets_colnames = ['Tweet ID', 'Full Text', 'Values', 'Start Index', 'End Index']

tweets = pd.DataFrame(tweets_cursor.fetchall(), columns=tweets_colnames)

def remove_values(df_row):
    full_text = df_row.at['Full Text']
    remove_vals = df_row.at['Values']
    start_index = df_row.at['Start Index']
    end_index = df_row.at['End Index']
    words = full_text.split()
    return [
        word for idx, word
        in enumerate(words)
        if not (
            word != remove_vals and
            start_index <= idx <= end_index
        )
    ]

#words_processed = df.apply(remove_values, axis=1)
remove_values(tweets)

import pandas as pd
from wordcloud import WordCloud

conn = sqlite3.connect('tweets.sqlite')
cur = conn.cursor()

## Read
tweets = cur.execute('SELECT e.tweet_id, t.full_text, e.value, e.start_index, e.end_index FROM Entities e join Tweets t on t.id = e.tweet_id')

df =pd.DataFrame(tweets, columns=['Tweet ID', 'Full Text', 'Values', 'Start Index', 'End Index'])
tweet_id = df['Tweet ID']
tweet = df['Full Text']


result = tweet.apply(preprocess_tweet, args=(tweet_id, tweet))

data = ' '.join(result)
wordcloud = WordCloud(width=800, height=400).generate(' '.join(data))
print(wordcloud)
