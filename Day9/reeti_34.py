# -*- coding: utf-8 -*-
"""
Created on Wed May 23 14:12:18 2018

@author: reeti
"""

import requests

data = {
        "Student Name":"REETI CHOUDHARY",
        "Student Age":"20",
        "Student Roll No":"15ESKCS142",
        "Student Branch":"CSE"
        }

send_url = "https://api.mlab.com/api/1/databases/mydb23/collections/info?apiKey=cUX5dh3W5SVQ3l2k0Fr369HQqi6eKe-t"
send_req = requests.post(send_url, json = data)
print send_req.text