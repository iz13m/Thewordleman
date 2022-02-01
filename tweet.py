# Importing necessary packages..
import tweepy

def tweet(twt):
    """
    This function takes only one argument, the tweet text.
    It uses Oauth1 credentials.
    """
    twitter_auth_keys = {
        "consumer_key"        : "*****",
        "consumer_secret"     : "*****",
        "access_token"        : "*****",
        "access_token_secret" : "*****"
    }

    auth = tweepy.OAuthHandler(
            twitter_auth_keys['consumer_key'],
            twitter_auth_keys['consumer_secret']
            )
    auth.set_access_token(
            twitter_auth_keys['access_token'],
            twitter_auth_keys['access_token_secret']
            )
    api = tweepy.API(auth)

    tweet = twt
    status = api.update_status(status=tweet)

if __name__ == "__main__":
    tweet("testing api .. Hello World!")
