import tweepy
from twitter_authentication import *
import pandas as pd

client = tweepy.Client(bearer_token=bearer_token,
                       consumer_key=consumer_key,
                       consumer_secret=consumer_secret,
                       access_token=access_token,
                       access_token_secret=access_token_secret,
                       wait_on_rate_limit=True)

network = {}
visited = {}
elon = client.get_user(id=44196397, user_fields='public_metrics')
elon_username = elon.data.username
elon_follower_count = elon.data.public_metrics['followers_count']
elon_id = elon.data.id
elon_followers = []
network[elon_id] = (elon_username, elon_follower_count, elon_followers)
print(network)
follower_names = client.get_users_followers(id=44196397, user_fields='public_metrics', max_results=10)
visited[elon_id] = True
for user in follower_names.data:
    network[elon_id][2].append(user.id)
    network[user.id] = (user.username, user.public_metrics['followers_count'], [])
print(network)
#     print(user.id)
# print(f"Follower Count: {elon}")
# likes = {}
#
# for tweet in response.data:
#     spotify_tweets.append(tweet)
#     likes[tweet.author_id] = client.get_liking_users(tweet.id)
# print(likes)
# result = []
# user_dict = {}
# # Loop through each response object
# for response in spotify_tweets:
#     # Take all of the users, and put them into a dictionary of dictionaries with the info we want to keep
#     for user in response.includes['users']:

#         user_dict[user.id] = {'username': user.username,
#                               'followers': user.public_metrics['followers_count'],
#                               'tweets': user.public_metrics['tweet_count'],
#                               'description': user.description,
#                               'location': user.location
#                               }
#     for tweet in response.data:
#         # For each tweet, find the author's information
#         author_info = user_dict[tweet.author_id]
#         # Put all of the information we want to keep in a single dictionary for each tweet
#         result.append({'author_id': tweet.author_id,
#                        'username': author_info['username'],
#                        'author_followers': author_info['followers'],
#                        'author_tweets': author_info['tweets'],
#                        'author_description': author_info['description'],
#                        'author_location': author_info['location'],
#                        'text': tweet.text,
#                        'created_at': tweet.created_at,
#                        'retweets': tweet.public_metrics['retweet_count'],
#                        'replies': tweet.public_metrics['reply_count'],
#                        'likes': tweet.public_metrics['like_count'],
#                        'quote_count': tweet.public_metrics['quote_count']
#                        })
#
# # Change this list of dictionaries into a dataframe
# df = pd.DataFrame(result)
# df.to_csv("Twitter.csv")
#
# # client = tweepy.Client(bearer_token="AAAAAAAAAAAAAAAAAAAAAEdbjAEAAAAARzRnLihwQ6jRC%2FDXOcsxF%2BPkUbE"
# #                                     "%3DFTsSVZERBrShHMqcGpcO65IxzDOFapZVqUMb4IRy1BC6ZjcmhZ",
# #                        consumer_key="1JA3ND1qukr6Lo5ygHowhYbyq",
# #                        consumer_secret="Zi0jcV1gChLofOBr4JWgmcWBVSvpz4UyvQKEfc4IJs0TYb9CZq",
# #                        access_token="1590065742807826432-AX1Fun3mawTwY65Z1yxOPCcX3olY04",
# #                        access_token_secret="n8DROuUaz3YBdPpHBgbQUrL8xqysUH97OkuQ0JiTkJF1P")
# #
# # query = '#nowplaying (good OR great OR fire OR happy OR exciting OR excited OR favorite OR fav OR amazing OR lovely ' \
# #         'OR incredible) (place_country:US OR place_country:MX OR place_country:CA) (min_faves:10) -horrible -worst ' \
# #         '-sucks -bad -disappointing'
# # query = '#nowplaying (good OR great OR fire OR happy OR exciting OR excited OR favorite OR fav OR amazing OR lovely ' \
# #         'OR incredible) -horrible -worst -sucks -bad -disappointing'
# #
# # likes = {}
# # for tweet in response.data:
# #     tmp = client.get_liking_users(tweet.id, max_results=10)
# #     # likes[tweet.author_id] = (tweet.text, [i.username for i in tmp.data])
# #     print(tweet.author_id)  # print the author id of the tweet
# #     print(tweet.public_metrics['like_count'])
# #     print(tweet.id)
# #     print(tweet.text)  # print the text
# #     # print(tmp)
