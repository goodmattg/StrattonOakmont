# General Scheduling in UCT (Zulu military time)
import pytz, random
import appAuth, twitpost
from datetime import datetime


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

        # IMPLEMENT RANDOM TWEET OR FAVORITE HERE
        sleep(random.randrange(1800,3600,10))


    sleep(60)  # sleep for a minute
