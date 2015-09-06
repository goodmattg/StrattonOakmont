# General Scheduling in UCT (Zulu military time)
import pytz, random
import appAuth, twitpost
from datetime import datetime

def changeSP():
    ticks = list()
    f = open('tickersSP.txt', 'r')
    for line in f:
        ticks.append(line)
    f.close()
    return ticks

def changeDJI():
    ticks = list()
    f = open('tickersDJI.txt', 'r')
    for line in f:
        ticks.append(line)
    f.close()
    return ticks

    # scheduler = sched.scheduler(time.time, time.sleep)
    # def print_event(name):
    #     print('EVENT: {0} {1}'.format(time.time(), name))

    # print('START: {0}'.format(time.time()))
    # scheduler.enter(2, 1, print_event, ('first',))
    # scheduler.enter(4, 1, print_event, ('second',))

    # scheduler.run()

    # gen = TweetGenerator([-1.1, 1.1, 0.3, -2.2, -0.4, 5], ["AAPL", "GOOG", "MSFT", "MMM", "CME", "CMI"])
    # gen.generateTweets()
    # tweet_list = gen.getTweetList()

    # twitter = TwitterAPI()
    # twitter.prep()
    # done_tweets = twitter.assignTweetsToFriends(tweet_list)
    # for d in done_tweets:
    #     twitter.tweet(d)

twitter = TwitterAPI()  # Initialize Twitter API interface
twitter.prep()  # Prepare interface with neccessary tokens/secrets/etc

while True:
    tcur = datetime.utcnow().replace(tzinfo = pytz.utc)  # get the current time (UTC)

    # 2.5 hours pre-trading day in UCT
    if (tcur.hour >= 11 and tcur.hour < 13) or (tcur.hour == 13 and tcur.minute < 30):
        twitGen = TweetGenerator([],[])

    # not in trading day
    else:
        if (random.randint(0,15) < 2):
            rand_friend = random.sample(set(twitter.api.friends_ids()), 1)[0]  # get a random friend
            last_tweet = twitter.api.user_timeline(rand_friend, count = 1)  # friend's last tweet ID

            if (random.randint(0,1)==0):
                twitter.api.create_favorite(last_tweet)  # favorite friend's tweet
            else:
                twitter.api.retweet(last_tweet)  # retweet friend's tweet



            # IMPLEMENT RANDOM TWEET OR FAVORITE HERE
        else:
            sleep(random.randrange(60))


    sleep(60)  # sleep for a minute
