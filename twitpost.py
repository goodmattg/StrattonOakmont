import pdb, tweepy, pickle
import sched, time
import random

class TwitterAPI:

    def __init__(self):

        self.consumer_key = None
        self.consumer_secret = None
        self.access_token = None
        self.access_token_secret = None
        self.FILE_consumer_key = "consumer_key.p"
        self.FILE_consumer_secret = "consumer_secret.p"
        self.FILE_access_token = "access_token.p"
        self.FILE_access_token_secret = "access_token_secret.p"

        self.prep() # Get all secrets/tokens from appropriate pickled files

        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)

        self.api = tweepy.API(auth)

    def _getconsumerkey(self):
        file = open(self.FILE_consumer_key, 'rb')
        self.consumer_key = str(pickle.load(file))
        file.close()
        return 1

    def _getconsumersecret(self):
        file = open(self.FILE_consumer_secret, 'rb')
        self.consumer_secret = str(pickle.load(file))
        file.close()
        return 1

    def _getaccesstoken(self):
        file = open(self.FILE_access_token, 'rb')
        self.access_token = str(pickle.load(file))
        file.close()
        return 1

    def _getaccesstokensecret(self):
        file = open(self.FILE_access_token_secret, 'rb')
        self.access_token_secret = str(pickle.load(file))
        file.close()
        return 1

    def prep(self):
        self._getconsumerkey()
        self._getconsumersecret()
        self._getaccesstoken()
        self._getaccesstokensecret()

    def assignTweetsToFriends(self, tweet_list):
        num_tweets = len(tweet_list)
        tweet_list = list(tweet_list)
        friend_set = set(self.api.friends_ids())  # returns list of friends
        friend_subset = random.sample(friend_set, num_tweets)  # subset of tweet size
        friend_subset = [self.api.get_user(ident).screen_name for ident in friend_subset] # friend numerical ID's to screen names

        # pdb.set_trace()

        random.shuffle(friend_subset)  # shuffle the friends
        random.shuffle(tweet_list)  # shuffle the tweets

        pairs = zip(tweet_list, friend_subset)  # zip friends and tweets into pairs

        complete_tweet_list = ["{0} @{1}".format(tweet,friend) for (tweet, friend) in pairs]
        return complete_tweet_list

    def tweet(self, message):
        self.api.update_status(status=message)


    #Standard order is initialize API, then prep(), then can make tweets



class TweetGenerator:

    pos_g1 = {"#slippageanticipated", "#stumbling", "#troubleahead"}
    pos_g2 = {"#drop", "#fallahead"}
    pos_g3 = {"#moderatedownside", "#ceasepurchase"}
    pos_g4 = {"#selloff", "#liquidateposition", "#liquidate"}
    pos_g5 = {"#bearmarket", "#highlypessimistic", "#collapse"}

    neg_g1 = {"#minorgains", "#upandcoming"}
    neg_g2 = {"#moderateupside", "#potentialgains"}
    neg_g3 = {"#significantupside", "#highlypromisingreturn"}
    neg_g4 = {"#buyimmedietly", "#loadup", "#capitalizenow"}
    neg_g5 = {"#bullmarket", "#rapidgains"}

    MAX_TWEET_CAP = 50

    def __init__(self, percent_list, stock_list):
        self.percent_list = percent_list
        self.stock_list = stock_list
        self.tweet_list = list()

    def generateTweets(self):
        for st in self.stock_list:

            ind = self.stock_list.index(st)
            perc = self.percent_list[ind]

            if (perc > 0 and perc < 0.5):
                self.tweet_list.append("{0} (ticker) experienced a {1} percent increase yesterday; today {2}".format(st, perc, random.sample(TweetGenerator.pos_g1, 1)[0]))
            elif (perc >= 0.5 and perc < 1):
                self.tweet_list.append("After a good day, {0} (ticker) should {1} in trading today.".format(st, random.sample(TweetGenerator.pos_g2, 1)[0]))

            elif (perc >= 1 and perc < 2):
                self.tweet_list.append("Following a strong {0} percent boost, we are seeing {1} today for stock {2} (ticker)".format(perc, random.sample(TweetGenerator.pos_g3, 1)[0], st))

            elif (perc >= 2 and perc < 4):
                self.tweet_list.append("{0} to avoid losses on {1} (ticker) during trading today.".format(random.sample(TweetGenerator.pos_g4, 1)[0], st))

            elif (perc >= 4):
                self.tweet_list.append("{0} (ticker) saw a blockbuster day, so we see {1} today.".format(st, random.sample(TweetGenerator.pos_g5, 1)[0]))

            elif perc <= 0 and perc > -0.5:
                self.tweet_list.append("{0} (ticker) experienced a {1} percent decrease yesterday; today {2}".format(st, perc, random.sample(TweetGenerator.neg_g1, 1)[0]))

            elif perc <= -0.5 and perc > -1:
                self.tweet_list.append("{0} (ticker) saw a slow day, so we see {1} today.".format(st, random.sample(TweetGenerator.neg_g2, 1)[0]))

            elif perc <= -1 and perc > -2:
                self.tweet_list.append("Following a weak {0} percent drop, we are seeing {1} for stock today.".format(perc, random.sample(TweetGenerator.neg_g3, 1)[0]))

            elif perc <= -2 and perc > -4:
                self.tweet_list.append("{0} during trading today to capitalize on gains for {1} (ticker)".format(random.sample(TweetGenerator.neg_g4, 1)[0], st))

            elif perc <= -4:
                self.tweet_list.append("After a very weak day, we are forecasting {0} today for {1} (ticker)".format(random.sample(TweetGenerator.neg_g5, 1)[0], st))

            else:
                print("Percent change not loaded")


    def getTweetList(self):
        return self.tweet_list






if __name__ == "__main__":






    gen = TweetGenerator([-1.1, 1.1, 0.3, -2.2, -0.4, 5], ["AAPL", "GOOG", "MSFT", "MMM", "CME", "CMI"])
    gen.generateTweets()
    tweet_list = gen.getTweetList()

    twitter = TwitterAPI()
    twitter.prep()
    done_tweets = twitter.assignTweetsToFriends(tweet_list)
    for d in done_tweets:
        twitter.tweet(d)
