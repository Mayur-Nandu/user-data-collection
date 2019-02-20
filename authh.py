import tweepy
##authentication


consumer_key='i2n1iF7QH5yXnmEjW50a7B8ha'
consumer_secret='WrbgvlphoBHcjTVPvEEe55jAFQSNYCz8BtVPnUpyv1oLsUXreY'
acces_token='2505249138-XcOz8fGKeeg4kvjoxeXaWkxh7XVdmt3wksAV3fk'
access_token_secret='PCZJ3BBa8dzIVVFL3XIVw4QqTjstUBcTgHnzge0Cnrm4x'
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(acces_token,access_token_secret)
##def authenticatee():
##api = tweepy.API(auth,wait_on_rate_limit=True)
api = tweepy.API(auth)
