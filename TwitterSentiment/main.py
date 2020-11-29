from flask import Flask,render_template,request,jsonify
import tweepy
from textblob import TextBlob


#---------------------------------------------------------------------------

consumer_key = 'nXlJZlaRn2tKUWOu0dHCJc62z'
consumer_secret = 'RSwu0RY7qQBqutcji7g9ZHoY6VgZCPR322nmoAr1ez68aAULuT'

access_token = '985446467296006144-5rs0a89Cw0GOFbXQo5Z9P3MegHI2ufF'
access_token_secret = 'JxquDRowdqodjHV5J3swBtQhGQdoTDe4gKbix6yCz1BTx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#-------------------------------------------------------------------------

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search",methods=["POST"])
def search():
    search_tweet = request.form.get("search_query")
    
    t = []
    tweets = api.search(search_tweet, tweet_mode='extended')
    for tweet in tweets:
        polarity = TextBlob(tweet.full_text).sentiment.polarity
        subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
        t.append([tweet.full_text,polarity,subjectivity])
        # t.append(tweet.full_text)

    return jsonify({"success":True,"tweets":t})

app.run()