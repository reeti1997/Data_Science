# -*- coding: utf-8 -*-
"""
Created on Thu May 17 13:03:40 2018

@author: reeti
"""

import requests

data = {
        "Phone_Number":"7877757144",
        "Name":"Kunal Vaid",
        "College_Name":"Amity University",
        "Branch":"B.Tech CSE"
        }

send_url = "http://13.127.155.43/api_v0.1/sending"
send_req = requests.post(send_url, json = data)
print send_req.text
#hepls us show the response

recieve_url = "http://13.127.155.43/api_v0.1/receiving?Phone_Number=7877757144"
recieve_req = requests.get(recieve_url)
print recieve_req.text