# General Scheduling in UCT (Zulu military time)
import pytz, random, pdb
import appAuth, twitpost
from datetime import datetime

def ticksSP():
    ticks = list()
    f = open('tickersSP.txt', 'r')
    for line in f:
        line = line.strip()
        ticks.append(line)
    f.close()
    return ticks


def ticksDJI():
    ticks = list()
    f = open('tickersDJI.txt', 'r')
    for line in f:
        line = line.strip()
        ticks.append(line)
    f.close()
    return ticks


# Functional but not practical. Too many API requests to Quandl.
def totSP(ticks):
    tot = 0
    for tick in ticks:
        tot = tot + appAuth.getPercDiff(tick, 7)
    return tot


def totDJI(ticks):
    tot = 0
    for tick in ticks:
        tot = tot + appAuth.getPercDiff(tick, 7)
    return tot




if __name__ == "__main__":

    twitter = twitpost.TwitterAPI()  # Initialize Twitter API interface
    twitter.prep()  # Prepare interface with neccessary tokens/secrets/etc
    ticks = ticksDJI()  # preprocess tickers


    while True:  # Run the bot for all time (or until program exited)

        tcur = datetime.utcnow().replace(tzinfo = pytz.utc)  # get the current time (UTC)

        # 2.5 hours pre-trading day in UCT
        if (tcur.hour >= 11 and tcur.hour < 13) or (tcur.hour == 13 and tcur.minute < 30):

            totdji = totDJI(ticks)
            dif = [appAuth.getPercDiff(t, 7) for t in ticks]

            # Append *special* Dow Jones composite
            dif.append(totdji)
            ticks.append("DJI")

            # Clear/Create Twitter Generator
            twitGen = twitpost.TweetGenerator(dif, ticks)

            # Generate Tweets
            twitGen.generateTweets()

            # Get the list of tweets
            tweets_list = twitGen.getTweetList()

            # Assign Tweets to friends
            done_tweets = twitter.assignTweetsToFriends(tweets_list)

            # POST Tweets at semi-random intervals
            for tw in done_tweets:
                twitter.tweet(tw)
                sleep(random.randint(120,150))

        # Trading day and normal business hours
        elif (tcur.hour >= 14 and tcur.hour < 20) :

            # Random action
            if (random.randint(0,30) < 2):
                # Isolate a random friend
                rand_friend = random.sample(set(twitter.api.friends_ids()), 1)[0]
                # Isolated friend's last tweet ID
                last_tweet = twitter.api.user_timeline(rand_friend, count = 1)

                # Favorite/Retweet friend's last post
                if (random.randint(0,1)==0):
                    twitter.api.create_favorite(last_tweet)
                else:
                    twitter.api.retweet(last_tweet)

            sleep(60)  # sleep for a minute


        # Non-standard hours. No activity.
        else:
            sleep(60)  # sleep for a minute

