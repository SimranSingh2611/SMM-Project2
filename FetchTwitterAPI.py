import tweepy
from tweepy.auth import OAuthHandler
from requests_oauthlib import  oauth1_auth
import pandas
import os
import requests

def write_to_csv(responses):
    user1 = []
    for response in responses:
        fields = {}
        response_dict = response.json()[0];

        for key, value in response_dict.items():
            if key in reqd_fields:
                fields[key] = value
        user1.append(fields)
        users_df = pandas.DataFrame(user1)

    user_data = open(os.getcwd() + '/user_data.csv', 'w')
    users_df.to_csv(user_data, index=False)
    user_data.close()



reqd_fields = ['id','id_str','screen_name','location','description','url',
                   'followers_count','friends_count', 'listed_count', 'created_at',
                   'favourites_count', 'verified','statuses_count','lang','status',
                   'default_profile','default_profile_image','has_extended_profile',
                   'name','bot']


if __name__ == "__main__":
    consumer_key = ""
    consumer_secret = ""

    access_token = ""
    access_token_secret = ""

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    #print(api.me().name)


    screen_name = ['obama','trump' ,'arizona', 'asu']
    responses = []
    for name in screen_name:
        response = requests.get(url="https://api.twitter.com/1.1/users/lookup.json?screen_name=" + str(name),
                                auth=auth)
        if response.status_code == 200:
            responses.append(response)
    write_to_csv(responses)

