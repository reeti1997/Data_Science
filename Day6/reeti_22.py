# -*- coding: utf-8 -*-
"""
Created on Fri May 18 11:27:30 2018

@author: reeti
"""

import urllib2
import oauth2
import time
import json

url1 = "https://api.twitter.com/1.1/search/tweets.json"  # FIXED AUTHENCATION PARAMETERS

params = {
        "oauth_version": "1.0",
        "oauth_nonce": oauth2.generate_nonce(),
        "oauth_timestamp": int(time.time())
    }

consumer = oauth2.Consumer(key="hnb7ozE3HSxwtt0UxupsphzDj", secret="j4JhnKvzEKBmuityerLlZYOXFpnj0JjopGqir9b6ZQ8lJuhur0")

token = oauth2.Token(key="997359596783124480-Vb39HNguoTBGjtgXazWT7FaB8INGOYw",
                     secret="0N503AGeX1gtoaS6KiuyLZtalXnbaA9d57iC0PJW5AtPN")

params["oauth_consumer_key"] = consumer.key   # VARIABLE AUTHENCATION PARAMETERS

params["oauth_token"] = token.key
params["q"]="jaipur"  # WHAT WE HAVE TO SEARCH

req = oauth2.Request(method="GET", url=url1, parameters=params)
signature_method = oauth2.SignatureMethod_HMAC_SHA1() 
#on line, the data should be encrypted so that its not visible to everyone.
# hence we use SHA
req.sign_request(signature_method, consumer, token)
url = req.to_url()
response = urllib2.Request(url)
data = json.load(urllib2.urlopen(response))

filename = params["q"]      
f = open(filename + "_File.txt", "w")  # SAVING DATA TO FILE
json.dump(data["statuses"], f)
f.close()