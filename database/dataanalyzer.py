#using ORM, define table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Enum, Float, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class TweetWordPair(Base):
    __tablename__ = 'tweet_word_pairs'
    
    tweet_id = Column(Integer, primary_key=True)
    word = Column(String)
    
from sqlalchemy import create_engine
engine = create_engine('sqlite:///tweets.db', echo=True)

Base.metadata.create_all(engine)
#TweetWordPair.__table__.drop(engine)

#fetch result from Q2b
preprocess
#to create
df = pd.DataFrame(wordcloud, columns=['Tweet ID', 'Full Text', 'Words'])
tweet_id = df['Tweet ID']
words = df['Words']

# Stack the dataframes to be used in table
wordRows = pd.concat([tweet_id, words], axis=0)

#connect dataframe with sqlalchemy table
wordRows.to_sql('TweetWordPair', con=engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

#to read
result = session.query(TweetWordPair)
for r in result:
    print(r)


############################################## UNUSED BELOW ##########################################

tweet = TweetWordPair(word="tweetssss")
session.add(tweet)
session.commit()

#to update from row
text = session.query(TweetWordPair).filter(TweetWordPair.word == "tweetsss")[0]
text.word = "another tweets"
session.commit()

#to delete
#tweet = TweetWordPair(word="tweetssss")
session.delete(tweet)
session.commit()