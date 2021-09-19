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
                            
# wordcloud visualization output:
print(wordcloud)

df = pd.DataFrame(wordcloud, columns=['Tweet ID', 'Full Text', 'Words'])
tweet_id = df['Tweet ID']
Words = df['Words']

# Stack the dataframes to be used in table
wordRows = pd.concat([tweet_id, words], axis=0)
display(wordRows)