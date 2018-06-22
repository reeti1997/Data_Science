# -*- coding: utf-8 -*-
"""
Created on Fri May 18 13:39:57 2018

@author: reeti
"""

import facebook as fb

# Facebook Graphic Explorer API user Access Token
# go to the link given
# get token (for v2.7)
# enable PUBLISH_ACTIONS permission
access_token = "EAACEdEose0cBAJo4AVokWZBexdscAUavS0yvEZCYhoKYnfNAzvsZCUTs9mhGSEVZCZAvl3XP6OPE4324NOio5xNKBEJ41ghDAnPr0f4B7YjN3RTlr7dlNsfirtNMsyBB7hN1KzVFraGUGT2EUcUA6yAuquriZCauHmnvCgHNvdyK4ZAo6pF2daT9zUZAjjVLZCwBi2EqEelhaAQZDZD"

# Message to post as status on Facebook
status = "Its all in the mind"

# Authenticating
graph = fb.GraphAPI(access_token)

# FUNCTION CALL FOR STATUS UPDATE
post_id = graph.put_wall_post(status)

# FUNCTION CALL FOR POSTINNG AN IMAGE
graph.put_photo(image = open("IMG_20180318_161740.jpg"), message = "You are a goddess living in a city of angels.")