# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 12:42:56 2018

@author: reeti
"""

from havenondemand.hodclient import *
import json
import pandas as pd

client = HODClient("63f13516-7ff4-4f9b-b7fb-67360cecf331", "v1") #apikey

#params = {'url': 'https://www.havenondemand.com/sample-content/videos/gb-plates.mp4', 'source_location': 'GB'} ##if using url
params = {'file': 'WhatsApp Video 2018-06-19 at 12.25.06 PM.mp4', 'source_location': 'IN'} ## or if using a local file
response_async = client.post_request(params, 'recognizelicenseplates', async=True)
jobID = response_async['jobID']
#print jobID

## Wait some time afterwards for async call to process...
response = client.get_job_result(jobID)
print response

#dump data in a json file
with open('data.json', 'w') as outfile:
    json.dump(response, outfile)